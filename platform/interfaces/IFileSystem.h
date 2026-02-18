#pragma once

#include <cstdint>
#include <string>
#include <vector>

namespace pvz::platform {

class IFileSystem {
public:
    virtual ~IFileSystem() = default;

    virtual bool Exists(const std::string& path) const = 0;
    virtual std::vector<std::uint8_t> ReadAllBytes(const std::string& path) const = 0;
};

} // namespace pvz::platform
