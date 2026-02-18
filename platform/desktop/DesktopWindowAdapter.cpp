#include "DesktopWindowAdapter.h"

namespace pvz::platform::desktop {

DesktopWindowAdapter::DesktopWindowAdapter(int width, int height)
    : mSize{width, height}
    , mTitle("web-plants-vs-zombies")
    , mCursorVisible(true)
    , mFullscreen(false)
{
}

WindowSize DesktopWindowAdapter::GetSize() const
{
    return mSize;
}

void DesktopWindowAdapter::SetTitle(const std::string& title)
{
    mTitle = title;
}

void DesktopWindowAdapter::SetCursorVisible(bool visible)
{
    mCursorVisible = visible;
}

void DesktopWindowAdapter::SetFullscreen(bool fullscreen)
{
    mFullscreen = fullscreen;
}

} // namespace pvz::platform::desktop
