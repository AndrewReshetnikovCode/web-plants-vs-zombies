#include "DesktopFileSystemAdapter.h"

#include <fstream>
#include <iterator>

namespace pvz::platform::desktop {

bool DesktopFileSystemAdapter::Exists(const std::string& path) const
{
    std::ifstream file(path, std::ios::binary);
    return file.good();
}

std::vector<std::uint8_t> DesktopFileSystemAdapter::ReadAllBytes(const std::string& path) const
{
    std::ifstream file(path, std::ios::binary);
    if (!file) {
        return {};
    }

    return std::vector<std::uint8_t>(std::istreambuf_iterator<char>(file), std::istreambuf_iterator<char>());
}

} // namespace pvz::platform::desktop
