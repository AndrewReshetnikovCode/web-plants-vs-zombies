#pragma once

#include "../interfaces/IAudio.h"

#include <string>

namespace pvz::platform::desktop {

class DesktopAudioAdapter : public IAudio {
public:
    void PlayMusic(const std::string& id, bool loop) override;
    void StopMusic() override;
    void PlaySfx(const std::string& id) override;
    void SetMasterVolume(float volume) override;

    const std::string& LastMusicId() const;
    const std::string& LastSfxId() const;
    float MasterVolume() const;

private:
    std::string mLastMusicId;
    std::string mLastSfxId;
    float mMasterVolume = 1.0f;
    bool mMusicLoop = false;
};

} // namespace pvz::platform::desktop
