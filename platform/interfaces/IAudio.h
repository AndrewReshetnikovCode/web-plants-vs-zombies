#pragma once

#include <string>

namespace pvz::platform {

class IAudio {
public:
    virtual ~IAudio() = default;

    virtual void PlayMusic(const std::string& id, bool loop) = 0;
    virtual void StopMusic() = 0;
    virtual void PlaySfx(const std::string& id) = 0;
    virtual void SetMasterVolume(float volume) = 0;
};

} // namespace pvz::platform
