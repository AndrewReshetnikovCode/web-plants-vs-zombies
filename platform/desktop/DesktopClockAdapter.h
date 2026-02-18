#pragma once

#include "../interfaces/IClock.h"

#include <cstdint>

namespace pvz::platform::desktop {

class DesktopClockAdapter : public IClock {
public:
    DesktopClockAdapter();

    std::uint64_t NowMilliseconds() const override;
    float DeltaSeconds() const override;

private:
    std::uint64_t mStartTimeMs;
};

} // namespace pvz::platform::desktop
