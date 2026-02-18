#pragma once

#include "../interfaces/IWindow.h"

#include <string>

namespace pvz::platform::desktop {

class DesktopWindowAdapter : public IWindow {
public:
    DesktopWindowAdapter(int width, int height);

    WindowSize GetSize() const override;
    void SetTitle(const std::string& title) override;
    void SetCursorVisible(bool visible) override;
    void SetFullscreen(bool fullscreen) override;

private:
    WindowSize mSize;
    std::string mTitle;
    bool mCursorVisible;
    bool mFullscreen;
};

} // namespace pvz::platform::desktop
