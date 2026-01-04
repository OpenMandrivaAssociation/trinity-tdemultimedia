%bcond clang 1
%bcond taglib 1
%bcond akode 1
%bcond libmad 1
%bcond xine 1
%bcond lame 1
%bcond mpeg 1
%bcond musicbrainz 0
%bcond audiofile 1

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 5

%define tde_pkg tdemultimedia
%define tde_prefix /opt/trinity

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Summary:	Multimedia applications for the Trinity Desktop Environment
Version:	%{tde_version}
Release:	%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Group:		Productivity/Multimedia/Sound/Utilities
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:	https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/core/%{tarball_name}-%{version}%{?preversion:~%{preversion}}.tar.xz
Source1:	%{name}-rpmlintrc

BuildSystem:    cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DINCLUDE_INSTALL_DIR=%{tde_prefix}/include/tde
BuildOption:    -DPKGCONFIG_INSTALL_DIR=%{tde_prefix}/%{_lib}/pkgconfig
BuildOption:    -DWITH_ALL_OPTIONS=ON -DWITH_ALSA=ON 
BuildOption:    -DWITH_CDPARANOIA=ON
BuildOption:    -DWITH_FLAC=ON
BuildOption:    -DWITH_GSTREAMER=ON
BuildOption:    -DWITH_KSCD_CDDA=ON
BuildOption:    -DWITH_THEORA=ON -DWITH_VORBIS=ON -DBUILD_ALL=ON
BuildOption:    -DWITH_ARTS_AKODE=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}
BuildOption:    -DWITH_ARTS_AUDIOFILE=%{!?with_audiofile:OFF}%{?with_audiofile:ON}
BuildOption:    -DWITH_ARTS_MPEGLIB=%{!?with_mpeg:OFF}%{?with_mpeg:ON}
BuildOption:    -DWITH_ARTS_XINE=%{!?with_xine:OFF}%{?with_xine:ON}
BuildOption:    -DWITH_LAME=%{!?with_lame:OFF}%{?with_lame:ON}
BuildOption:    -DWITH_MUSICBRAINZ=%{!?with_musicbrainz:OFF}%{?with_musicbrainz:ON}
BuildOption:    -DWITH_TAGLIB=%{!?with_taglib:OFF}%{?with_taglib:ON}

Obsoletes:	trinity-kdemultimedia < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdemultimedia = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdemultimedia-libs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdemultimedia-libs = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdemultimedia-extras < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdemultimedia-extras = %{?epoch:%{epoch}:}%{version}-%{release}
Obsoletes:	trinity-kdemultimedia-extras-libs < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdemultimedia-extras-libs = %{?epoch:%{epoch}:}%{version}-%{release}

BuildRequires:	trinity-arts-devel >= %{tde_epoch}:1.5.10
BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	fdupes
BuildRequires:	desktop-file-utils

# TAGLIB support
%{?with_taglib:BuildRequires: pkgconfig(taglib)}

# AKODE support
%{?with_akode:BuildRequires: trinity-akode-devel}

# MAD support
%ifarch %{ix86} %{x86_64}
%{?with_libmad:BuildRequires: libakode_mpeg_decoder}
%endif

# ZLIB support
BuildRequires:	pkgconfig(zlib)

# MUSICBRAINZ support
## not currently compatible with libtunepimp-0.5 (only libtunepimp-0.4)
#define with_musicbrainz 1
#BuildRequires: libmusicbrainz-devel libtunepimp-devel

# Audio libraries
%{?with_audiofile:BuildRequires:	pkgconfig(audiofile)}

BuildRequires:	cdparanoia

# VORBIS support
BuildRequires:  pkgconfig(vorbis)


# THEORA
BuildRequires:  pkgconfig(theora)

# ALSA support
BuildRequires:  pkgconfig(alsa)

# CDDA support
BuildRequires:	%{_lib}cdda-devel

# CDIO support
BuildRequires:	pkgconfig(libcdio)
BuildRequires:	pkgconfig(libcdio_paranoia)

# FLAC support
BuildRequires:  pkgconfig(flac)

# GSTREAMER support
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-plugins-base-1.0)

# X11 Libraries
BuildRequires:	pkgconfig(xxf86dga)
BuildRequires:	pkgconfig(xxf86vm)

# XINE support
%{?with_xine:BuildRequires:  pkgconfig(libxine)}

# LAME support
%{?with_lame:BuildRequires:		pkgconfig(lame)}

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

# ACL support
BuildRequires:  pkgconfig(libacl)

# ATTR support
BuildRequires:  pkgconfig(libattr)

BuildRequires:  pkgconfig(xrender)


Requires: trinity-artsbuilder = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-juk = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kaboodle = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kaudiocreator = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-kfile-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-kappfinder-data = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: %{name}-tdeio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-tdemid = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kmix = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-krec = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: trinity-kscd = %{?epoch:%{epoch}:}%{version}-%{release}
%{?with_akode:Requires: trinity-libarts-akode = %{?epoch:%{epoch}:}%{version}-%{release}}
%{?with_audiofile:Requires: trinity-libarts-audiofile = %{?epoch:%{epoch}:}%{version}-%{release}}
%{?with_mpeg:Requires: trinity-libarts-mpeglib = %{?epoch:%{epoch}:}%{version}-%{release}}
%{?with_xine:Requires: trinity-libarts-xine = %{?epoch:%{epoch}:}%{version}-%{release}}
Requires: trinity-libkcddb = %{?epoch:%{epoch}:}%{version}-%{release}
%{?with_mpeg:Requires: trinity-mpeglib = %{?epoch:%{epoch}:}%{version}-%{release}}
Requires: trinity-noatun = %{?epoch:%{epoch}:}%{version}-%{release}


%description
The Trinity Desktop Environment (TDE) is a GUI desktop for the X Window
System. The tdemultimedia package contains multimedia applications for
TDE, including:
  artsbuilder, Synthesizer designer for aRts
  juk, a media player
  tdemid, a midi player
  kmix, an audio mixer
  arts, additional functionality for the aRts sound system
  krec, a recording tool
  kscd, an Audio-CD player
  kaudiocreator, a graphical frontend for audio file creation 
  kaboodle, a media player
  noatun, a media player

%files

##########

%package -n trinity-artsbuilder
Summary:	Synthesizer designer for aRts
Group:		Productivity/Multimedia/Sound/Mixers
Requires:	trinity-kicker >= %{tde_version}

%description -n trinity-artsbuilder
This is the analog Realtime synthesizer's graphical design tool.

%files -n trinity-artsbuilder
%defattr(-,root,root,-)
%{tde_prefix}/bin/artsbuilder
%{tde_prefix}/bin/artscontrol
%{tde_prefix}/bin/midisend
%{tde_prefix}/%{_lib}/libartsbuilder.la
%{tde_prefix}/%{_lib}/libartsbuilder.so.*
%{tde_prefix}/%{_lib}/libartscontrolapplet.la
%{tde_prefix}/%{_lib}/libartscontrolapplet.so.*
%{tde_prefix}/%{_lib}/libartscontrolsupport.la
%{tde_prefix}/%{_lib}/libartscontrolsupport.so.*
%{tde_prefix}/%{_lib}/libartsgui_idl.la
%{tde_prefix}/%{_lib}/libartsgui_idl.so.*
%{tde_prefix}/%{_lib}/libartsgui_kde.la
%{tde_prefix}/%{_lib}/libartsgui_kde.so.*
%{tde_prefix}/%{_lib}/libartsgui.la
%{tde_prefix}/%{_lib}/libartsgui.so.*
%{tde_prefix}/%{_lib}/libartsmidi_idl.la
%{tde_prefix}/%{_lib}/libartsmidi_idl.so.*
%{tde_prefix}/%{_lib}/libartsmidi.la
%{tde_prefix}/%{_lib}/libartsmidi.so.*
%{tde_prefix}/%{_lib}/libartsmodulescommon.la
%{tde_prefix}/%{_lib}/libartsmodulescommon.so.*
%{tde_prefix}/%{_lib}/libartsmoduleseffects.la
%{tde_prefix}/%{_lib}/libartsmoduleseffects.so.*
%{tde_prefix}/%{_lib}/libartsmodulesmixers.la
%{tde_prefix}/%{_lib}/libartsmodulesmixers.so.*
%{tde_prefix}/%{_lib}/libartsmodules.la
%{tde_prefix}/%{_lib}/libartsmodules.so.*
%{tde_prefix}/%{_lib}/libartsmodulessynth.la
%{tde_prefix}/%{_lib}/libartsmodulessynth.so.*
%{tde_prefix}/%{_lib}/mcop/Arts/ArtsBuilderLoader.mcopclass
%{tde_prefix}/%{_lib}/mcop/artsbuilder.mcopclass
%{tde_prefix}/%{_lib}/mcop/artsbuilder.mcoptype
%{tde_prefix}/%{_lib}/mcop/Arts/Button.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/EffectRackGuiFactory.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Effect_WAVECAPTURE.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Environment/Container.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Environment/EffectRackItem.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Environment/InstrumentItemGuiFactory.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Environment/InstrumentItem.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Environment/MixerItem.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Fader.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/FiveBandMonoComplexEQGuiFactory.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/FiveBandMonoComplexEQ.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/FreeverbGuiFactory.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/GenericGuiFactory.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/GraphLine.mcopclass
%{tde_prefix}/%{_lib}/mcop/artsgui.mcopclass
%{tde_prefix}/%{_lib}/mcop/artsgui.mcoptype
%{tde_prefix}/%{_lib}/mcop/Arts/HBox.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Label.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/LayoutBox.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/LevelMeter.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/LineEdit.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/LittleStereoMixerChannelGuiFactory.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/LittleStereoMixerChannel.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/LocalFactory.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/MidiManager.mcopclass
%{tde_prefix}/%{_lib}/mcop/artsmidi.mcopclass
%{tde_prefix}/%{_lib}/mcop/artsmidi.mcoptype
%{tde_prefix}/%{_lib}/mcop/Arts/MixerGuiFactory.mcopclass
%{tde_prefix}/%{_lib}/mcop/artsmodulescommon.mcopclass
%{tde_prefix}/%{_lib}/mcop/artsmodulescommon.mcoptype
%{tde_prefix}/%{_lib}/mcop/artsmoduleseffects.mcopclass
%{tde_prefix}/%{_lib}/mcop/artsmoduleseffects.mcoptype
%{tde_prefix}/%{_lib}/mcop/artsmodules.mcopclass
%{tde_prefix}/%{_lib}/mcop/artsmodules.mcoptype
%{tde_prefix}/%{_lib}/mcop/artsmodulesmixers.mcopclass
%{tde_prefix}/%{_lib}/mcop/artsmodulesmixers.mcoptype
%{tde_prefix}/%{_lib}/mcop/artsmodulessynth.mcopclass
%{tde_prefix}/%{_lib}/mcop/artsmodulessynth.mcoptype
%{tde_prefix}/%{_lib}/mcop/Arts/MonoSimpleMixerChannelGuiFactory.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/MonoSimpleMixerChannel.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/MonoToStereo.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/PopupBox.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Poti.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/SimpleMixerChannelGuiFactory.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/SimpleMixerChannel.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/SpinBox.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/StereoBalanceGuiFactory.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/StereoBalance.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/StereoCompressorGuiFactory.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/StereoFirEqualizerGuiFactory.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/StereoToMono.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/StereoVolumeControlGuiFactory.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/StereoVolumeControlGui.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/StructureBuilder.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/StructureDesc.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_ATAN_SATURATE.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_AUTOPANNER.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_BRICKWALL_LIMITER.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_CAPTURE_WAV.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_CDELAY.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_COMPRESSOR.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_DATA.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_DEBUG.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_DELAY.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_DIV.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_ENVELOPE_ADSR.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_FM_SOURCE.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_FREEVERB.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_FX_CFLANGER.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_MIDI_DEBUG.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_MIDI_TEST.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_MOOG_VCF.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_NIL.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_NOISE.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_OSC.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_PITCH_SHIFT_FFT.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_PITCH_SHIFT.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_PLAY_PAT.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_PSCALE.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_RC.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_SEQUENCE_FREQ.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_SEQUENCE.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_SHELVE_CUTOFF.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_STD_EQUALIZER.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_STEREO_COMPRESSOR.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_STEREO_FIR_EQUALIZER.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_STEREO_PITCH_SHIFT_FFT.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_STEREO_PITCH_SHIFT.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_TREMOLO.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_VOICE_REMOVAL.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_WAVE_PULSE.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_WAVE_SOFTSAW.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_WAVE_SQUARE.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_WAVE_TRI.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Synth_XFADE.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/VBox.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/VoiceRemovalGuiFactory.mcopclass
%{tde_prefix}/%{_lib}/mcop/Arts/Widget.mcopclass
%{tde_prefix}/share/applications/tde/artsbuilder.desktop
%{tde_prefix}/share/applications/tde/artscontrol.desktop
%{tde_prefix}/share/apps/artsbuilder/
%{tde_prefix}/share/apps/artscontrol/
%{tde_prefix}/share/apps/kicker/applets/artscontrolapplet.desktop
%{tde_prefix}/share/icons/crystalsvg/*/actions/artsaudiomanager.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/artsbuilderexecute.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/artsenvironment.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/artsfftscope.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/artsmediatypes.png
%{tde_prefix}/share/icons/crystalsvg/*/actions/artsmidimanager.png
%{tde_prefix}/share/icons/crystalsvg/scalable/actions/artsaudiomanager.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/actions/artsenvironment.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/actions/artsfftscope.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/actions/artsmediatypes.svgz
%{tde_prefix}/share/icons/crystalsvg/scalable/actions/artsmidimanager.svgz
%{tde_prefix}/share/icons/hicolor/*/apps/artsbuilder.png
%{tde_prefix}/share/icons/hicolor/*/apps/artscontrol.png
%{tde_prefix}/share/icons/hicolor/scalable/apps/artsbuilder.svgz
%{tde_prefix}/share/icons/hicolor/scalable/apps/artscontrol.svgz
%{tde_prefix}/share/mimelnk/application/x-artsbuilder.desktop
%{tde_prefix}/share/doc/tde/HTML/en/artsbuilder/

##########

%package -n trinity-juk
Summary:	Music organizer and player for Trinity
Group:		Productivity/Multimedia/Sound/Players

%description -n trinity-juk
JuK (pronounced "jook") is a jukebox and music manager for the TDE
desktop similar to jukebox software on other platforms such as
iTunes or RealOne.

Some of JuK's features include:
* Support for Ogg Vorbis and MP3 formats
* Tag editing support for both formats, including ID3v2 for MP3 files.
  Multitagging or editing a selection of multiple files at once is also
  supported
* Output to either the aRts, default KDE sound system, or GStreamer
* Management of your "collection" and multiple playlists
* Import and export to m3u playlists
* Binary caching of audio meta-data and playlist information for faster
  load times (starting with the second time you run JuK)
* Integration into TDE that allows drag-and-drop and clipboard usage
  with other TDE and X apps

%files -n trinity-juk
%defattr(-,root,root,-)
%{tde_prefix}/bin/juk
%{tde_prefix}/share/applications/tde/juk.desktop
%{tde_prefix}/share/apps/juk/
%{tde_prefix}/share/apps/konqueror/servicemenus/jukservicemenu.desktop
%{tde_prefix}/share/icons/crystalsvg/*/actions/juk_dock.png
%{tde_prefix}/share/icons/hicolor/*/apps/juk.png
%{tde_prefix}/share/doc/tde/HTML/en/juk/
%{tde_prefix}/share/man/man1/juk.1*

##########

%package -n trinity-kaboodle
Summary:	Light, embedded media player for Trinity
Group:		System/GUI/Other

%if %{with xine}
Requires:	trinity-libarts-xine = %{?epoch:%{epoch}:}%{version}-%{release}
%endif

%description -n trinity-kaboodle
Kaboodle is a light, embedded media player, supporting both video and audio,
for TDE. It uses the aRts framework for playing media files.

%files -n trinity-kaboodle
%defattr(-,root,root,-)
%{tde_prefix}/bin/kaboodle
%{tde_prefix}/%{_lib}/trinity/libkaboodlepart.la
%{tde_prefix}/%{_lib}/trinity/libkaboodlepart.so
%{tde_prefix}/share/applications/tde/kaboodle.desktop
%{tde_prefix}/share/apps/kaboodle/
%{tde_prefix}/share/icons/hicolor/*/apps/kaboodle.png
%{tde_prefix}/share/services/kaboodle_component.desktop
%{tde_prefix}/share/services/kaboodleengine.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kaboodle/
%{tde_prefix}/share/man/man1/kaboodle.1*

##########

%package -n trinity-kaudiocreator
Summary:	CD ripper and audio encoder frontend for Trinity
Group:		Productivity/Multimedia/CD/Grabbers

Requires:	%{name}-tdeio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	vorbis-tools
Requires:	flac

%description -n trinity-kaudiocreator
KAudioCreator is a tool for audio extraction (ripping) and encoding. It can
keep your WAV files, or convert them to Ogg/Vorbis, MP3, or FLAC. It also
searches CDDB to retrieve the information of the disk.

%files -n trinity-kaudiocreator
%defattr(-,root,root,-)
%{tde_prefix}/bin/kaudiocreator
%{tde_prefix}/share/applications/tde/kaudiocreator.desktop
%{tde_prefix}/share/apps/kaudiocreator/
%{tde_prefix}/share/apps/tdeconf_update/kaudiocreator-libkcddb.upd
%{tde_prefix}/share/apps/tdeconf_update/kaudiocreator-meta.upd
%{tde_prefix}/share/apps/tdeconf_update/upgrade-kaudiocreator-metadata.sh
%{tde_prefix}/share/apps/konqueror/servicemenus/audiocd_extract.desktop
%{tde_prefix}/share/config.kcfg/kaudiocreator.kcfg
%{tde_prefix}/share/config.kcfg/kaudiocreator_encoders.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kaudiocreator.png
%{tde_prefix}/share/icons/locolor/*/apps/kaudiocreator.png
%{tde_prefix}/share/doc/tde/HTML/en/kaudiocreator/
%{tde_prefix}/share/man/man1/kaudiocreator.1*

##########

%package kfile-plugins
Summary:	An au/avi/m3u/mp3/ogg/wav plugins for kfile
Group:		Productivity/Multimedia/Sound/Utilities

%description kfile-plugins
au/avi/m3u/mp3/ogg/wav file metainformation plugins for Trinity.

%files kfile-plugins
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/tdefile_au.la
%{tde_prefix}/%{_lib}/trinity/tdefile_au.so
%{tde_prefix}/%{_lib}/trinity/tdefile_avi.la
%{tde_prefix}/%{_lib}/trinity/tdefile_avi.so
%{tde_prefix}/%{_lib}/trinity/tdefile_flac.la
%{tde_prefix}/%{_lib}/trinity/tdefile_flac.so
%{tde_prefix}/%{_lib}/trinity/tdefile_m3u.la
%{tde_prefix}/%{_lib}/trinity/tdefile_m3u.so
%{tde_prefix}/%{_lib}/trinity/tdefile_mp3.la
%{tde_prefix}/%{_lib}/trinity/tdefile_mp3.so
%{tde_prefix}/%{_lib}/trinity/tdefile_mp4.la
%{tde_prefix}/%{_lib}/trinity/tdefile_mp4.so
%{tde_prefix}/%{_lib}/trinity/tdefile_mpc.la
%{tde_prefix}/%{_lib}/trinity/tdefile_mpc.so
%{tde_prefix}/%{_lib}/trinity/tdefile_mpeg.la
%{tde_prefix}/%{_lib}/trinity/tdefile_mpeg.so
%{tde_prefix}/%{_lib}/trinity/tdefile_ogg.la
%{tde_prefix}/%{_lib}/trinity/tdefile_ogg.so
%{tde_prefix}/%{_lib}/trinity/tdefile_sid.la
%{tde_prefix}/%{_lib}/trinity/tdefile_sid.so
%{tde_prefix}/%{_lib}/trinity/tdefile_theora.la
%{tde_prefix}/%{_lib}/trinity/tdefile_theora.so
%{tde_prefix}/%{_lib}/trinity/tdefile_wav.la
%{tde_prefix}/%{_lib}/trinity/tdefile_wav.so
%{tde_prefix}/share/services/tdefile_au.desktop
%{tde_prefix}/share/services/tdefile_avi.desktop
%{tde_prefix}/share/services/tdefile_flac.desktop
%{tde_prefix}/share/services/tdefile_m3u.desktop
%{tde_prefix}/share/services/tdefile_mp3.desktop
%{tde_prefix}/share/services/tdefile_mp4.desktop
%{tde_prefix}/share/services/tdefile_mpc.desktop
%{tde_prefix}/share/services/tdefile_mpeg.desktop
%{tde_prefix}/share/services/tdefile_ogg.desktop
%{tde_prefix}/share/services/tdefile_sid.desktop
%{tde_prefix}/share/services/tdefile_theora.desktop
%{tde_prefix}/share/services/tdefile_wav.desktop

##########

%package kappfinder-data
Summary:	Multimedia data for kappfinder
Group:		Productivity/Multimedia/Sound/Utilities

Requires: 	trinity-kappfinder >= %{tde_version}
Requires:	trinity-tdebase-runtime-data-common >= %{tde_version}

%description kappfinder-data
This package provides data on multimedia applications for kappfinder.

%files kappfinder-data
%defattr(-,root,root,-)
%{tde_prefix}/share/apps/kappfinder/
%{tde_prefix}/share/desktop-directories/tde-multimedia-music.directory
%config %{_sysconfdir}/xdg/menus/applications-merged/tde-multimedia-music.menu

##########

%package tdeio-plugins
Summary:	Enables the browsing of audio CDs under Konqueror
Group:		Productivity/Multimedia/Sound/Utilities
Requires:	trinity-tdebase-tdeio-plugins >= %{tde_version}

Obsoletes:	trinity-tdemultimedia-kio-plugins < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-tdemultimedia-kio-plugins = %{?epoch:%{epoch}:}%{version}-%{release}

%description tdeio-plugins
This package allow audio CDs to be browsed like a file system using
Konqueror and the audiocd:/ URL.

%files tdeio-plugins
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/kcm_audiocd.la
%{tde_prefix}/%{_lib}/trinity/kcm_audiocd.so
%{tde_prefix}/%{_lib}/trinity/tdeio_audiocd.la
%{tde_prefix}/%{_lib}/trinity/tdeio_audiocd.so
%{tde_prefix}/%{_lib}/trinity/libaudiocd_encoder_flac.la
%{tde_prefix}/%{_lib}/trinity/libaudiocd_encoder_flac.so
%{tde_prefix}/%{_lib}/trinity/libaudiocd_encoder_lame.la
%{tde_prefix}/%{_lib}/trinity/libaudiocd_encoder_lame.so
%{tde_prefix}/%{_lib}/trinity/libaudiocd_encoder_vorbis.la
%{tde_prefix}/%{_lib}/trinity/libaudiocd_encoder_vorbis.so
%{tde_prefix}/%{_lib}/trinity/libaudiocd_encoder_wav.la
%{tde_prefix}/%{_lib}/trinity/libaudiocd_encoder_wav.so
%{tde_prefix}/%{_lib}/libaudiocdplugins.so.*
%{tde_prefix}/share/applications/tde/audiocd.desktop
%{tde_prefix}/share/apps/tdeconf_update/audiocd.upd
%{tde_prefix}/share/apps/tdeconf_update/upgrade-metadata.sh
%{tde_prefix}/share/config.kcfg/audiocd_lame_encoder.kcfg
%{tde_prefix}/share/config.kcfg/audiocd_vorbis_encoder.kcfg
%{tde_prefix}/share/services/audiocd.protocol
%{tde_prefix}/share/doc/tde/HTML/en/tdeioslave/audiocd/
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/audiocd/

##########

%package -n trinity-tdemid
Summary:	MIDI/karaoke player for Trinity
Group:		Productivity/Multimedia/Sound/Midi

Obsoletes:	trinity-kmid < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kmid = %{?epoch:%{epoch}:}%{version}-%{release}

%description -n trinity-tdemid
This package provides a MIDI and karaoke player for TDE.

%files -n trinity-tdemid
%defattr(-,root,root,-)
%{tde_prefix}/bin/tdemid
%{tde_prefix}/%{_lib}/trinity/libtdemidpart.la
%{tde_prefix}/%{_lib}/trinity/libtdemidpart.so
%{tde_prefix}/%{_lib}/libtdemidlib.so.*
%{tde_prefix}/share/applications/tde/tdemid.desktop
%{tde_prefix}/share/apps/tdemid/
%{tde_prefix}/share/icons/hicolor/*/apps/tdemid.png
%{tde_prefix}/share/mimelnk/audio/x-karaoke.desktop
%{tde_prefix}/share/servicetypes/audiomidi.desktop
%{tde_prefix}/share/doc/tde/HTML/en/tdemid/

##########

%package -n trinity-kmix
Summary:	Sound mixer applet for Trinity
Group:		Productivity/Multimedia/Sound/Mixers
Requires:	trinity-kicker >= %{tde_version}

%description -n trinity-kmix
This package includes TDE's dockable sound mixer applet.

%files -n trinity-kmix
%defattr(-,root,root,-)
%{tde_prefix}/bin/kmix
%{tde_prefix}/bin/kmixctrl
%{tde_prefix}/%{_lib}/trinity/kmix.la
%{tde_prefix}/%{_lib}/trinity/kmix.so
%{tde_prefix}/%{_lib}/trinity/kmix_panelapplet.la
%{tde_prefix}/%{_lib}/trinity/kmix_panelapplet.so
%{tde_prefix}/%{_lib}/trinity/kmixctrl.la
%{tde_prefix}/%{_lib}/trinity/kmixctrl.so
%{tde_prefix}/%{_lib}/libtdeinit_kmix.so
%{tde_prefix}/%{_lib}/libtdeinit_kmixctrl.so
%{tde_prefix}/share/applications/tde/kmix.desktop
%{tde_prefix}/share/apps/kicker/applets/kmixapplet.desktop
%{tde_prefix}/share/apps/kmix/
%{tde_prefix}/share/autostart/kmix.desktop
%{tde_prefix}/share/autostart/restore_kmix_volumes.desktop
%{tde_prefix}/share/icons/hicolor/*/apps/kmix.png
%{tde_prefix}/share/services/kmixctrl_restore.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kmix/
%{tde_prefix}/share/man/man1/kmix.1*
%{tde_prefix}/share/man/man1/kmixctrl.1*

##########

%package -n trinity-krec
Summary:	Sound recorder utility for Trinity
Group:		Productivity/Multimedia/CD/Record

%description -n trinity-krec
This is a sound recording utility for Trinity.

%files -n trinity-krec
%defattr(-,root,root,-)
%{tde_prefix}/bin/krec
%{tde_prefix}/%{_lib}/trinity/kcm_krec.la
%{tde_prefix}/%{_lib}/trinity/kcm_krec.so
%{tde_prefix}/%{_lib}/trinity/kcm_krec_files.la
%{tde_prefix}/%{_lib}/trinity/kcm_krec_files.so
%{tde_prefix}/%{_lib}/trinity/krec.la
%{tde_prefix}/%{_lib}/trinity/krec.so
%if %{with lame}
%{tde_prefix}/%{_lib}/trinity/libkrecexport_mp3.la
%{tde_prefix}/%{_lib}/trinity/libkrecexport_mp3.so
%{tde_prefix}/share/services/krec_exportmp3.desktop
%endif
%{tde_prefix}/%{_lib}/trinity/libkrecexport_ogg.la
%{tde_prefix}/%{_lib}/trinity/libkrecexport_ogg.so
%{tde_prefix}/%{_lib}/trinity/libkrecexport_wave.la
%{tde_prefix}/%{_lib}/trinity/libkrecexport_wave.so
%{tde_prefix}/%{_lib}/libtdeinit_krec.so
%{tde_prefix}/share/applications/tde/krec.desktop
%{tde_prefix}/share/apps/krec/
%{tde_prefix}/share/icons/hicolor/*/apps/krec.png
%{tde_prefix}/share/services/kcm_krec.desktop
%{tde_prefix}/share/services/kcm_krec_files.desktop
%{tde_prefix}/share/services/krec_exportogg.desktop
%{tde_prefix}/share/services/krec_exportwave.desktop
%{tde_prefix}/share/servicetypes/krec_exportitem.desktop
%{tde_prefix}/share/doc/tde/HTML/en/krec/
%{tde_prefix}/share/man/man1/krec.1*

##########

%package -n trinity-kscd
Summary:	Audio CD player for Trinity
Group:		Productivity/Multimedia/CD/Players

%description -n trinity-kscd
This is Trinity's audio CD player.

%files -n trinity-kscd
%defattr(-,root,root,-)
%{tde_prefix}/bin/kscd
%{tde_prefix}/bin/workman2cddb.pl
%{tde_prefix}/share/applications/tde/kscd.desktop
%{tde_prefix}/share/apps/konqueror/servicemenus/audiocd_play.desktop
%{tde_prefix}/share/apps/kscd/
%{tde_prefix}/share/apps/profiles/kscd.profile.xml
%{tde_prefix}/share/config.kcfg/kscd.kcfg
%{tde_prefix}/share/icons/hicolor/*/apps/kscd.png
%{tde_prefix}/share/mimelnk/text/xmcd.desktop
%{tde_prefix}/share/doc/tde/HTML/en/kscd/

##########

%if %{with akode}
%package -n trinity-libarts-akode
Summary:	Akode plugin for aRts
Group:		Productivity/Multimedia/Other

%description -n trinity-libarts-akode
This package contains akode plugins for aRts.

%files -n trinity-libarts-akode
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libarts_akode.so.*
%{tde_prefix}/%{_lib}/libarts_akode.la
%{tde_prefix}/%{_lib}/mcop/akodearts.mcoptype
%{tde_prefix}/%{_lib}/mcop/akodearts.mcopclass
%{tde_prefix}/%{_lib}/mcop/akodeMPCPlayObject.mcopclass
%{tde_prefix}/%{_lib}/mcop/akodePlayObject.mcopclass
%{tde_prefix}/%{_lib}/mcop/akodeSpeexStreamPlayObject.mcopclass
%{tde_prefix}/%{_lib}/mcop/akodeVorbisStreamPlayObject.mcopclass
%{tde_prefix}/%{_lib}/mcop/akodeXiphPlayObject.mcopclass

# Requires MAD support
%if %{with libmad}
%{tde_prefix}/%{_lib}/mcop/akodeMPEGPlayObject.mcopclass
%endif

%endif

##########

%package -n trinity-libarts-audiofile
Summary:	Audiofile plugin for aRts
Group:		Productivity/Multimedia/Other

%description -n trinity-libarts-audiofile
This package contains audiofile plugins for aRts.

%files -n trinity-libarts-audiofile
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/libarts_audiofile.so.*
%{tde_prefix}/%{_lib}/libarts_audiofile.la
%{tde_prefix}/%{_lib}/mcop/Arts/audiofilePlayObject.mcopclass
%{tde_prefix}/%{_lib}/mcop/audiofilearts.mcopclass
%{tde_prefix}/%{_lib}/mcop/audiofilearts.mcoptype

##########

%if %{with mpeg}

%package -n trinity-libarts-mpeglib
Summary:	Mpeglib plugin for aRts, supporting mp3 and mpeg audio/video
Group:		Productivity/Multimedia/Other

%description -n trinity-libarts-mpeglib
This package contains the mpeglib aRts plugin, supporting mp3 and mpeg
audio and video.

This is the arts (TDE Sound daemon) plugin.

%files -n trinity-libarts-mpeglib
%defattr(-,root,root,-)
%{tde_prefix}/bin/mpeglibartsplay
%{tde_prefix}/%{_lib}/libarts_mpeglib-0.3.0.so.*
%{tde_prefix}/%{_lib}/libarts_mpeglib.la
%{tde_prefix}/%{_lib}/libarts_splay.so.*
%{tde_prefix}/%{_lib}/libarts_splay.la
%{tde_prefix}/%{_lib}/mcop/CDDAPlayObject.mcopclass
%{tde_prefix}/%{_lib}/mcop/MP3PlayObject.mcopclass
%{tde_prefix}/%{_lib}/mcop/NULLPlayObject.mcopclass
%{tde_prefix}/%{_lib}/mcop/OGGPlayObject.mcopclass
%{tde_prefix}/%{_lib}/mcop/SplayPlayObject.mcopclass
%{tde_prefix}/%{_lib}/mcop/WAVPlayObject.mcopclass

%endif

##########

%if %{with xine}
%package -n trinity-libarts-xine
Summary:	ARTS plugin enabling xine support
Group:		Productivity/Multimedia/Other

%description -n trinity-libarts-xine
This package contains aRts' xine plugin, allowing the use of the xine
multimedia engine though aRts.

%files -n trinity-libarts-xine
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/videothumbnail.la
%{tde_prefix}/%{_lib}/trinity/videothumbnail.so
%{tde_prefix}/%{_lib}/libarts_xine.so.*
%{tde_prefix}/%{_lib}/libarts_xine.la
%{tde_prefix}/%{_lib}/mcop/xineAudioPlayObject.mcopclass
%{tde_prefix}/%{_lib}/mcop/xineVideoPlayObject.mcopclass
%{tde_prefix}/share/apps/videothumbnail/sprocket-large.png
%{tde_prefix}/share/apps/videothumbnail/sprocket-medium.png
%{tde_prefix}/share/apps/videothumbnail/sprocket-small.png
%{tde_prefix}/share/services/videothumbnail.desktop

%endif

##########

%package -n trinity-libkcddb
Summary:	CDDB library for Trinity
Group:		Productivity/Multimedia/Other
Requires:	trinity-kcontrol >= %{tde_version}

%description -n trinity-libkcddb
The Trinity native CDDB (CD Data Base) library, providing easy access to Audio
CD meta-information (track titles, artist information, etc.) from on-line
databases, for TDE applications.

%files -n trinity-libkcddb
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/kcm_cddb.la
%{tde_prefix}/%{_lib}/trinity/kcm_cddb.so
%{tde_prefix}/%{_lib}/libkcddb.so.*
%{tde_prefix}/share/applications/tde/libkcddb.desktop
%{tde_prefix}/share/apps/tdeconf_update/kcmcddb-emailsettings.upd
%{tde_prefix}/share/config.kcfg/libkcddb.kcfg
%{tde_prefix}/share/doc/tde/HTML/en/kcontrol/cddb/

##########

%if %{with mpeg}

%package -n trinity-mpeglib
Summary:	MP3 and MPEG-1 audio and video library
Group:		Productivity/Multimedia/Other
%if 0%{?with_mpeg}
Requires:	trinity-libarts-mpeglib = %{?epoch:%{epoch}:}%{version}-%{release}
%endif

%description -n trinity-mpeglib
mpeglib is a MPEG-1 and MP3 audio and video library. It supports
MPEG-1 audio (layers 1, 2, 3), MPEG-1 video, MPEG-1 system layer,
and WAV playback

%files -n trinity-mpeglib
%defattr(-,root,root,-)
%{tde_prefix}/bin/yaf-cdda
%{tde_prefix}/bin/yaf-mpgplay
%{tde_prefix}/bin/yaf-splay
%{tde_prefix}/bin/yaf-tplay
%{tde_prefix}/bin/yaf-vorbis
%{tde_prefix}/bin/yaf-yuv
%{tde_prefix}/%{_lib}/libmpeg-0.3.0.so
%{tde_prefix}/%{_lib}/libyafcore.so
%{tde_prefix}/%{_lib}/libyafxplayer.so

%endif

##########

%package -n trinity-noatun
Summary:	Media player for Trinity
Group:		Productivity/Multimedia/Video/Players
Requires:	trinity-tdebase-bin >= %{tde_version}

# 20120802: Hack to avoid dependency issue on MGA2 and MDV2011
Provides:	devel(libnoatunarts)
Provides:	devel(libnoatunarts(64bit))

%description -n trinity-noatun
Noatun is an aRts-based audio and video player for Trinity. It supports all
formats supported by your installation of aRts (including aRts plugins).

%files -n trinity-noatun
%defattr(-,root,root,-)
%{tde_prefix}/bin/noatun
%{tde_prefix}/%{_lib}/tdeconf_update_bin/noatun20update
%{tde_prefix}/%{_lib}/trinity/noatun.la
%{tde_prefix}/%{_lib}/trinity/noatun.so
%{tde_prefix}/%{_lib}/trinity/noatun_dcopiface.la
%{tde_prefix}/%{_lib}/trinity/noatun_dcopiface.so
%{tde_prefix}/%{_lib}/trinity/noatun_excellent.la
%{tde_prefix}/%{_lib}/trinity/noatun_excellent.so
%{tde_prefix}/%{_lib}/trinity/noatun_htmlexport.la
%{tde_prefix}/%{_lib}/trinity/noatun_htmlexport.so
%{tde_prefix}/%{_lib}/trinity/noatun_infrared.la
%{tde_prefix}/%{_lib}/trinity/noatun_infrared.so
%{tde_prefix}/%{_lib}/trinity/noatun_kaiman.la
%{tde_prefix}/%{_lib}/trinity/noatun_kaiman.so
%{tde_prefix}/%{_lib}/trinity/noatun_keyz.la
%{tde_prefix}/%{_lib}/trinity/noatun_keyz.so
%{tde_prefix}/%{_lib}/trinity/noatun_kjofol.la
%{tde_prefix}/%{_lib}/trinity/noatun_kjofol.so
%{tde_prefix}/%{_lib}/trinity/noatun_marquis.la
%{tde_prefix}/%{_lib}/trinity/noatun_marquis.so
%{tde_prefix}/%{_lib}/trinity/noatun_metatag.la
%{tde_prefix}/%{_lib}/trinity/noatun_metatag.so
%{tde_prefix}/%{_lib}/trinity/noatun_monoscope.la
%{tde_prefix}/%{_lib}/trinity/noatun_monoscope.so
%{tde_prefix}/%{_lib}/trinity/noatun_net.la
%{tde_prefix}/%{_lib}/trinity/noatun_net.so
%{tde_prefix}/%{_lib}/trinity/noatun_splitplaylist.la
%{tde_prefix}/%{_lib}/trinity/noatun_splitplaylist.so
%{tde_prefix}/%{_lib}/trinity/noatun_systray.la
%{tde_prefix}/%{_lib}/trinity/noatun_systray.so
%{tde_prefix}/%{_lib}/trinity/noatun_ui.la
%{tde_prefix}/%{_lib}/trinity/noatun_ui.so
%{tde_prefix}/%{_lib}/trinity/noatun_voiceprint.la
%{tde_prefix}/%{_lib}/trinity/noatun_voiceprint.so
%{tde_prefix}/%{_lib}/trinity/noatun_winskin.la
%{tde_prefix}/%{_lib}/trinity/noatun_winskin.so
%{tde_prefix}/%{_lib}/trinity/noatunsimple.la
%{tde_prefix}/%{_lib}/trinity/noatunsimple.so
%{tde_prefix}/%{_lib}/libartseffects.la
%{tde_prefix}/%{_lib}/libartseffects.so
%{tde_prefix}/%{_lib}/libtdeinit_noatun.so
%{tde_prefix}/%{_lib}/libnoatun.so.*
%{tde_prefix}/%{_lib}/libnoatunarts.la
%{tde_prefix}/%{_lib}/libnoatunarts.so
%{tde_prefix}/%{_lib}/libnoatuncontrols.so.*
%{tde_prefix}/%{_lib}/libnoatuntags.so.*
%{tde_prefix}/%{_lib}/libwinskinvis.la
%{tde_prefix}/%{_lib}/libwinskinvis.so
%{tde_prefix}/%{_lib}/mcop/ExtraStereo.mcopclass
%{tde_prefix}/%{_lib}/mcop/ExtraStereoGuiFactory.mcopclass
%{tde_prefix}/%{_lib}/mcop/Noatun/
%{tde_prefix}/%{_lib}/mcop/RawWriter.mcopclass
%{tde_prefix}/%{_lib}/mcop/VoiceRemoval.mcopclass
%{tde_prefix}/%{_lib}/mcop/artseffects.mcopclass
%{tde_prefix}/%{_lib}/mcop/artseffects.mcoptype
%{tde_prefix}/%{_lib}/mcop/noatunarts.mcopclass
%{tde_prefix}/%{_lib}/mcop/noatunarts.mcoptype
%{tde_prefix}/%{_lib}/mcop/winskinvis.mcopclass
%{tde_prefix}/%{_lib}/mcop/winskinvis.mcoptype
%{tde_prefix}/share/applications/tde/noatun.desktop
%{tde_prefix}/share/apps/tdeconf_update/noatun.upd
%{tde_prefix}/share/apps/noatun/
%{tde_prefix}/share/icons/hicolor/*/apps/noatun.png
%{tde_prefix}/share/mimelnk/interface/x-winamp-skin.desktop
%{tde_prefix}/share/doc/tde/HTML/en/noatun/
%{tde_prefix}/share/man/man1/noatun.1*

##########

%package devel
Summary:	Development files for %{name}, aRts and noatun plugins
Group:		Development/Libraries/Other
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires:	trinity-tdelibs-devel >= %{tde_version}

Obsoletes:	trinity-kdemultimedia-devel < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-kdemultimedia-devel = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
{summary}.

Install %{name}-devel if you wish to develop or compile any
applications using aRtsbuilder, aRtsmidi, aRtskde, aRts modules or
noatun plugins.

%files devel
%defattr(-,root,root,-)
%{tde_prefix}/include/*
%if %{with akode}
%{tde_prefix}/%{_lib}/libarts_akode.so
%endif
%{tde_prefix}/%{_lib}/libarts_audiofile.so
%if %{with mpeg}
%{tde_prefix}/%{_lib}/libarts_mpeglib.so
%{tde_prefix}/%{_lib}/libarts_mpeglib-0.3.0.so
%{tde_prefix}/%{_lib}/libarts_splay.so
%endif
%if %{with xine}
%{tde_prefix}/%{_lib}/libarts_xine.so
%endif
%{tde_prefix}/%{_lib}/libartsbuilder.so
%{tde_prefix}/%{_lib}/libartscontrolapplet.so
%{tde_prefix}/%{_lib}/libartscontrolsupport.so
%{tde_prefix}/%{_lib}/libartsgui.so
%{tde_prefix}/%{_lib}/libartsgui_idl.so
%{tde_prefix}/%{_lib}/libartsgui_kde.so
%{tde_prefix}/%{_lib}/libartsmidi.so
%{tde_prefix}/%{_lib}/libartsmidi_idl.so
%{tde_prefix}/%{_lib}/libartsmodules.so
%{tde_prefix}/%{_lib}/libartsmodulescommon.so
%{tde_prefix}/%{_lib}/libartsmoduleseffects.so
%{tde_prefix}/%{_lib}/libartsmodulesmixers.so
%{tde_prefix}/%{_lib}/libartsmodulessynth.so
%{tde_prefix}/%{_lib}/libaudiocdplugins.la
%{tde_prefix}/%{_lib}/libaudiocdplugins.so
%{tde_prefix}/%{_lib}/libkcddb.la
%{tde_prefix}/%{_lib}/libkcddb.so
%{tde_prefix}/%{_lib}/libtdeinit_kmix.la
%{tde_prefix}/%{_lib}/libtdeinit_kmixctrl.la
%{tde_prefix}/%{_lib}/libtdeinit_krec.la
%{tde_prefix}/%{_lib}/libtdeinit_noatun.la
%{tde_prefix}/%{_lib}/libtdemidlib.la
%{tde_prefix}/%{_lib}/libtdemidlib.so
%if %{with mpeg}
%{tde_prefix}/%{_lib}/libmpeg.la
%{tde_prefix}/%{_lib}/libmpeg.so
%endif
%{tde_prefix}/%{_lib}/libnoatun.la
%{tde_prefix}/%{_lib}/libnoatun.so
%{tde_prefix}/%{_lib}/libnoatuncontrols.la
%{tde_prefix}/%{_lib}/libnoatuncontrols.so
%{tde_prefix}/%{_lib}/libnoatuntags.la
%{tde_prefix}/%{_lib}/libnoatuntags.so
%if %{with mpeg}
%{tde_prefix}/%{_lib}/libyafcore.la
%{tde_prefix}/%{_lib}/libyafxplayer.la
%endif

%prep -a
%__sed -i "tdeioslave/audiocd/kcmaudiocd/audiocd.desktop" -e "s|^Icon=.*|Icon=kcmaudio|"


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig:${PKG_CONFIG_PATH}"

%install -p
export PATH="%{tde_prefix}/bin:${PATH}"

%install -a
# Disable MPEG support entirely
%if %{without mpeg}
%__rm %{?buildroot}%{tde_prefix}/bin/mpeglibartsplay
%__rm %{?buildroot}%{tde_prefix}/bin/yaf-*
%__rm %{?buildroot}%{tde_prefix}/%{_lib}/libarts_mpeglib*
%__rm %{?buildroot}%{tde_prefix}/%{_lib}/libarts_splay.*
%__rm %{?buildroot}%{tde_prefix}/%{_lib}/libmpeg*
%__rm %{?buildroot}%{tde_prefix}/%{_lib}/libyaf*
%__rm %{?buildroot}%{tde_prefix}/%{_lib}/mcop/MP3PlayObject.mcopclass
%__rm %{?buildroot}%{tde_prefix}/%{_lib}/mcop/CDDAPlayObject.mcopclass
%__rm %{?buildroot}%{tde_prefix}/%{_lib}/mcop/NULLPlayObject.mcopclass
%__rm %{?buildroot}%{tde_prefix}/%{_lib}/mcop/OGGPlayObject.mcopclass
%__rm %{?buildroot}%{tde_prefix}/%{_lib}/mcop/SplayPlayObject.mcopclass
%__rm %{?buildroot}%{tde_prefix}/%{_lib}/mcop/WAVPlayObject.mcopclass
%endif

# Links duplicate files
%fdupes "%{?buildroot}%{tde_prefix}/share"

