#include "DesktopClockAdapter.h"

#include <chrono>

namespace pvz::platform::desktop {
namespace {
std::uint64_t CurrentTimeMs()
{
    const auto now = std::chrono::steady_clock::now().time_since_epoch();
    return static_cast<std::uint64_t>(std::chrono::duration_cast<std::chrono::milliseconds>(now).count());
}
} // namespace

DesktopClockAdapter::DesktopClockAdapter()
    : mStartTimeMs(CurrentTimeMs())
{
}

std::uint64_t DesktopClockAdapter::NowMilliseconds() const
{
    return CurrentTimeMs();
}

float DesktopClockAdapter::DeltaSeconds() const
{
    const std::uint64_t elapsed = CurrentTimeMs() - mStartTimeMs;
    return static_cast<float>(elapsed) / 1000.0f;
}

} // namespace pvz::platform::desktop
