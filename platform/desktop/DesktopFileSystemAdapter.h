#pragma once

#include "../interfaces/IFileSystem.h"

namespace pvz::platform::desktop {

class DesktopFileSystemAdapter : public IFileSystem {
public:
    bool Exists(const std::string& path) const override;
    std::vector<std::uint8_t> ReadAllBytes(const std::string& path) const override;
};

} // namespace pvz::platform::desktop
