#pragma once

namespace pvz::platform {

enum class MouseButton {
    Left,
    Right,
    Middle
};

class IInput {
public:
    virtual ~IInput() = default;

    virtual bool IsKeyDown(int keycode) const = 0;
    virtual bool IsMouseButtonDown(MouseButton button) const = 0;
    virtual int GetMouseX() const = 0;
    virtual int GetMouseY() const = 0;
};

} // namespace pvz::platform
