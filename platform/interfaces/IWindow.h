#pragma once

#include <string>

namespace pvz::platform {

struct WindowSize {
    int width;
    int height;
};

class IWindow {
public:
    virtual ~IWindow() = default;

    virtual WindowSize GetSize() const = 0;
    virtual void SetTitle(const std::string& title) = 0;
    virtual void SetCursorVisible(bool visible) = 0;
    virtual void SetFullscreen(bool fullscreen) = 0;
};

} // namespace pvz::platform
