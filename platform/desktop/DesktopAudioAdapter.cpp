#include "DesktopAudioAdapter.h"

namespace pvz::platform::desktop {

void DesktopAudioAdapter::PlayMusic(const std::string& id, bool loop)
{
    mLastMusicId = id;
    mMusicLoop = loop;
}

void DesktopAudioAdapter::StopMusic()
{
    mLastMusicId.clear();
    mMusicLoop = false;
}

void DesktopAudioAdapter::PlaySfx(const std::string& id)
{
    mLastSfxId = id;
}

void DesktopAudioAdapter::SetMasterVolume(float volume)
{
    mMasterVolume = volume;
}

const std::string& DesktopAudioAdapter::LastMusicId() const
{
    return mLastMusicId;
}

const std::string& DesktopAudioAdapter::LastSfxId() const
{
    return mLastSfxId;
}

float DesktopAudioAdapter::MasterVolume() const
{
    return mMasterVolume;
}

} // namespace pvz::platform::desktop
