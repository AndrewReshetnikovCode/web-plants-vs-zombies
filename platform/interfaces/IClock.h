#pragma once

#include <cstdint>

namespace pvz::platform {

class IClock {
public:
    virtual ~IClock() = default;

    virtual std::uint64_t NowMilliseconds() const = 0;
    virtual float DeltaSeconds() const = 0;
};

} // namespace pvz::platform
