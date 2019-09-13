#
# spec file for package kadu
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012-2018 Mariusz Fik <fisiu@opensuse.org>.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define real    %{name}-%{version}
%define build_penguins 0

Name:           kadu
Version:        4.3
Release:        0
# Choosing GPL-3.0+ because of presence and usage of numerous GPL-3.0 files
Summary:        Gadu-Gadu and Jabber/XMPP protocol Instant Messenger
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Instant Messenger
Url:            http://www.kadu.im/
Source0:        http://download.kadu.im/stable/%{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM fix-gcc7.patch fisiu@opensuse.org -- fix compilation with gcc7
Patch7:         fix-gcc7.patch
# PATCH-FEATURE-OPENSUSE enable_external_plugins.patch fisiu@opensuse.org -- not ready yet for kadu >= 4
Patch0:         enable_external_plugins.patch
# PATCH-FIX-UPSTREAM 0001-fix_SDK_DIR.patch sfalken@opensuse.org -- fixed CMake Buildfailure
Patch1:         0001-fix_SDK_DIR.patch
# PATCH-FIX-OPENSUSE libqxmpp-qt5-fix.patch fisiu@opensuse.org
Patch100:       libqxmpp-qt5-fix.patch
### 1x - External Plugins ### not ready yet for kadu >= 4
Source10:       http://download.kadu.im/external-plugins/2.0/anonymous_check-2.0.1.tar.bz2
Source11:       http://download.kadu.im/external-plugins/2.0/import_history-2.0.tar.bz2
Source12:       http://download.kadu.im/external-plugins/2.0/kadu_completion-2.0.tar.bz2
Source13:       http://download.kadu.im/external-plugins/2.0/mime_tex-2.0.tar.bz2
### 2x - Emoticons ###
%if %{build_penguins}
Source20:       kompatybilne_z_GG6.tar.gz
Source21:       gg10_compatible.tar.bz2
%endif
### 3x - Sounds ###
Source30:       kadu-sound-bns.tar.bz2
Source31:       kadu-sound-drums.tar.bz2
Source32:       kadu-sound-florkus.tar.bz2
Source33:       kadu-sound-michalsrodek.tar.bz2
Source34:       kadu-sound-percussion.tar.bz2
Source35:       kadu-sound-ultr.tar.bz2
BuildRequires:  cmake >= 2.8.11
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libgcrypt-devel
BuildRequires:  libqt5-linguist-devel >= 5.2
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(Qt5Concurrent) >= 5.2
BuildRequires:  pkgconfig(Qt5Core) >= 5.2
BuildRequires:  pkgconfig(Qt5DBus) >= 5.2
BuildRequires:  pkgconfig(Qt5Multimedia) >= 5.2
BuildRequires:  pkgconfig(Qt5Network) >= 5.2
BuildRequires:  pkgconfig(Qt5Script) >= 5.2
BuildRequires:  pkgconfig(Qt5Sql) >= 5.2
BuildRequires:  pkgconfig(Qt5WebKit) >= 5.2
BuildRequires:  pkgconfig(Qt5WebKitWidgets) >= 5.2
BuildRequires:  pkgconfig(Qt5Widgets) >= 5.2
BuildRequires:  pkgconfig(Qt5X11Extras) >= 5.2
BuildRequires:  pkgconfig(Qt5Xml) >= 5.2
BuildRequires:  pkgconfig(Qt5XmlPatterns) >= 5.2
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(enchant)
BuildRequires:  pkgconfig(injeqt) >= 1.2
BuildRequires:  pkgconfig(libarchive) >= 2.6.0
BuildRequires:  pkgconfig(libgadu) >= 1.12.2
BuildRequires:  pkgconfig(libidn)
BuildRequires:  pkgconfig(libotr) >= 4.0
BuildRequires:  pkgconfig(phonon4qt5)
BuildRequires:  pkgconfig(qca2-qt5)
BuildRequires:  pkgconfig(qxmpp-qt5) >= 0.8.3
BuildRequires:  pkgconfig(sndfile)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xscrnsaver)
BuildRequires:  pkgconfig(zlib)
# runtime requires
Requires:       libgadu3 >= 1.12.2
# sql_history plugin needs qt5-sqlite to operate
Requires:       libQt5Sql5-sqlite
# packages dropped in kadu-2.0
Obsoletes:      globalhotkeys
Obsoletes:      lednotify
Obsoletes:      messagessplitter
Obsoletes:      networkping
Obsoletes:      nextinfo
Obsoletes:      panelkadu
Obsoletes:      senthistory
# packages dropped in kadu-4.0
Obsoletes:      anonymous_check
Obsoletes:      completion
Obsoletes:      import_history
Obsoletes:      mimetex
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Kadu is an open source Gadu-Gadu and Jabber/XMPP protocol Instant Messenger
client for Linux, BSD, Mac OS X and Windows. Kadu depends on Qt library
version 5.2. Kadu supports KDE, GNOME and Window Maker as well.
The core of Kadu is the libgadu library (its role being handling the network layer).

%package        devel
Summary:        Gadu-Gadu and Jabber/XMPP protocol Instant Messenger
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description    devel
Kadu is an open source Gadu-Gadu and Jabber/XMPP protocol Instant Messenger
client for Linux, BSD, Mac OS X and Windows. Kadu depends on Qt library
version 5.2. Kadu supports KDE, GNOME and Window Maker as well.
The core of Kadu is the libgadu library (its role being handling the network layer).

Files mandatory for development.

### External Plugins ###
# %package        anonymous_check
# Summary:        Automatic lookup of an interlocutor in public directory
# License:        GPL-3.0+
# Group:          Productivity/Networking/Instant Messenger
# Requires:       %{name} = %{version}

# %description    anonymous_check
# Anonymous_check is a plugin to automatic lookup who is an interlocutor
# when (s)he starts talking to you.

# %package        completion
# Summary:        Bash completion-like module for Kadu
# License:        GPL-3.0+
# Group:          Productivity/Networking/Instant Messenger
# Requires:       %{name} = %{version}

# %description    completion
# Bash completion-like module for Kadu.

# %package        import_history
# Summary:        History import plugin
# License:        GPL-3.0+
# Group:          Productivity/Networking/Instant Messenger
# Requires:       %{name} = %{version}

# %description    import_history
# History import plugins allows to import history from Gadu-Gadu 7, 8.

# %package        mimetex
# Summary:        TeX formulas support
# License:        GPL-3.0+
# Group:          Productivity/Networking/Instant Messenger
# Requires:       %{name} = %{version}

# %description    mimetex
# Mime_tex is a plugin to edit TeX mathematic formulas in chat window.

### Emoticons ###
%if %{build_penguins}

%package        emoticons_gg6_compatible
Summary:        Emoticons theme compatybility witch Gadu-Gadu 6
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Instant Messenger
Requires:       %{name} = %{version}

%description    emoticons_gg6_compatible
Emoticons theme compatybility witch Gadu-Gadu 6.0 and olders.

%package        emoticons_gg10_compatible
Summary:        Emoticons theme compatybility witch Gadu-Gadu 10
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Instant Messenger
Requires:       %{name} = %{version}

%description    emoticons_gg10_compatible
Emoticons theme compatybility witch Gadu-Gadu 10.0 and olders.
http://kde-look.org/content/show.php/gadu+gadu+10?content=118930
%endif

### Sounds ###

%package        sound-bns
Summary:        Bns sound theme for Kadu
License:        CC-BY-NC-SA-2.5
Group:          Productivity/Networking/Instant Messenger
Requires:       %{name} = %{version}

%description    sound-bns
Bns sound theme by bns <banasio@o2.pl> | http://www.banas.ovh.org

%package        sound-drums
Summary:        Drums sound theme for Kadu
License:        CC-BY-NC-SA-3.0
Group:          Productivity/Networking/Instant Messenger
Requires:       %{name} = %{version}

%description    sound-drums
Drums sound theme by Konrad (ancestor) Strack <konrad.strack@gmail.com>

%package        sound-florkus
Summary:        Florkus sound theme for Kadu
License:        CC-BY-NC-SA-3.0
Group:          Productivity/Networking/Instant Messenger
Requires:       %{name} = %{version}

%description    sound-florkus
Florkus sound theme by florkus <florkusthewhite@gmail.com>

%package        sound-michalsrodek
Summary:        Michalsrodek sound theme for Kadu
License:        CC-BY-NC-SA-3.0
Group:          Productivity/Networking/Instant Messenger
Requires:       %{name} = %{version}

%description    sound-michalsrodek
Michalsrodek sound theme by Michał Środek files trans i transsend: florkus <florkusthewhite@gmail.com>

%package        sound-percussion
Summary:        Percussion sound theme for Kadu
License:        CC-BY-NC-SA-3.0
Group:          Productivity/Networking/Instant Messenger
Requires:       %{name} = %{version}

%description    sound-percussion
Percussion sound theme by Konrad (ancestor) Strack <konrad.strack@gmail.com>

%package        sound-ultr
Summary:        Ultr sound theme for Kadu
License:        CC-BY-SA-1.0
Group:          Productivity/Networking/Instant Messenger
Requires:       %{name} = %{version}

%description    sound-ultr
Ultr sound theme collected by Piotr "ultr" Dąbrowski
error.wav: http://www.freesound.org/samplesViewSingle.php?id=27422
  by hello_flowers
filefinished.wav: http://www.freesound.org/samplesViewSingle.php?id=56229
  by pera
fileincoming.wav: http://www.freesound.org/samplesViewSingle.php?id=32951
  by HardPCM
newchat.wav: http://www.freesound.org/samplesViewSingle.php?id=26777
  by junggle
newmessage.wav: http://www.pdsounds.org/sounds/blip
  by Natalie
status.wav: http://www.pdsounds.org/sounds/clickick_switch
  by Stephan

%prep
%setup -q -n %{real}
# add external plugins
# %setup -qTD -a10 -a11 -a12 -a13 -n %{real}/plugins
# add additionals emoticons
%if %{build_penguins}
%setup -qTD -a20 -a21 -n %{real}/varia/themes/emoticons
%endif
# add additionals sound themes
%setup -qTD -a30 -a31 -a32 -a33 -a34 -a35 -n %{real}/varia/themes/sounds
#
%setup -qDTn %{real}
%patch7 -p0
# enable external plugins (patch0):
#
# anonymous_check, completion, importhistory, mime_tex
#
# %patch0
%patch1 -p1
%patch100

# fix qxmpp include path
sed -e 's:<qxmpp/:<qxmpp-qt5/:' -i plugins/jabber_protocol/{,*/}*.{h,cpp}

# switch state of internal plugins
# don't enable mpd since it's not in oss repository
sed -e 's:\t\tmpd_mediaplayer:\t\t# mpd_mediaplayer:' -i Plugins.cmake
# disable unity related plugin
sed -e 's:\t\tunity_integration:\t\t# unity_integration:' -i Plugins.cmake
sed -e 's:\t\tindicator_docking:\t\t# indicator_docking:' -i Plugins.cmake

# enable additionals emoticons
%if %{build_penguins}
sed -e "s:\ttango:\ttango\n\tgg6_compatible\n\tgg10_compatible:" -i varia/themes/emoticons/CMakeLists.txt
%endif
# enable additionals sound themes
sed -e "s:\tdefault:\tdefault\n\tbns\n\tdrums\n\tflorkus\n\tmichalsrodek\n\tpercussion\n\tultr:" \
    -i varia/themes/sounds/CMakeLists.txt

%build
cmake \
%if %{_lib} == "lib64"
      -DLIB_SUFFIX=64 \
%endif
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DWITH_ENCHANT=ON \
      -DENABLE_TESTS=OFF \
      -DINSTALL_UNOFFICIAL_TRANSLATIONS=ON \
      -DQCA_SUFFIX:STRING=qt5
make %{?_smp_mflags}

%install
%make_install

%fdupes %{buildroot}%{_prefix}
%suse_update_desktop_file -r kadu Network InstantMessaging

# Don't check RPATH
export NO_BRP_CHECK_RPATH=true

%post
# none

%postun
# none

%files
%defattr(-,root,root)
%{_bindir}/kadu
%{_datadir}/applications/kadu.desktop
%dir %{_libdir}/kadu
%dir %{_libdir}/kadu/plugins
%dir %{_datadir}/kadu
%dir %{_datadir}/kadu/configuration
%dir %{_datadir}/kadu/plugins
%dir %{_datadir}/kadu/plugins/configuration
%dir %{_datadir}/kadu/plugins/data
%dir %{_datadir}/kadu/plugins/data/antistring
%dir %{_datadir}/kadu/plugins/data/cenzor
%dir %{_datadir}/kadu/plugins/data/gadu_protocol
%dir %{_datadir}/kadu/plugins/data/mediaplayer
%dir %{_datadir}/kadu/plugins/data/mprisplayer_mediaplayer
%dir %{_datadir}/kadu/plugins/data/sms
%dir %{_datadir}/kadu/plugins/data/sms/scripts
%dir %{_datadir}/kadu/plugins/data/sql_history
%dir %{_datadir}/kadu/plugins/data/sql_history/scripts
%dir %{_datadir}/kadu/plugins/data/word_fix
%dir %{_datadir}/kadu/plugins/translations
%dir %{_datadir}/kadu/scripts
%dir %{_datadir}/kadu/syntax
%dir %{_datadir}/kadu/syntax/chat
%dir %{_datadir}/kadu/syntax/infopanel
%dir %{_datadir}/kadu/themes
%dir %{_datadir}/kadu/themes/emoticons
%dir %{_datadir}/kadu/themes/emoticons/penguins
%dir %{_datadir}/kadu/themes/emoticons/tango
%dir %{_datadir}/kadu/themes/icons
%dir %{_datadir}/kadu/themes/sounds
%dir %{_datadir}/kadu/translations
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/icons/hicolor/*
%dir %{_datadir}/icons/hicolor/*/apps
%{_datadir}/icons/hicolor/*/apps/kadu.png
%{_datadir}/kadu/AUTHORS
%{_datadir}/kadu/AUTHORS.html
%{_datadir}/kadu/ChangeLog
%{_datadir}/kadu/ChangeLog.OLD-PL
%{_datadir}/kadu/COPYING.GPL2
%{_datadir}/kadu/COPYING.LGPL2.1
%{_datadir}/kadu/HISTORY
%{_datadir}/kadu/README
%{_datadir}/kadu/THANKS
%{_datadir}/kadu/configuration/dialog-look-chat-advanced.ui
%{_datadir}/kadu/configuration/dialog.ui
%{_datadir}/kadu/plugins/antistring.desc
%{_datadir}/kadu/plugins/autoaway.desc
%{_datadir}/kadu/plugins/auto_hide.desc
%{_datadir}/kadu/plugins/autoresponder.desc
%{_datadir}/kadu/plugins/autostatus.desc
%{_datadir}/kadu/plugins/cenzor.desc
%{_datadir}/kadu/plugins/chat_notify.desc
%{_datadir}/kadu/plugins/config_wizard.desc
%{_datadir}/kadu/plugins/docking.desc
%{_datadir}/kadu/plugins/docking_notify.desc
%{_datadir}/kadu/plugins/emoticons.desc
%{_datadir}/kadu/plugins/encryption_otr.desc
%{_datadir}/kadu/plugins/exec_notify.desc
%{_datadir}/kadu/plugins/ext_sound.desc
%{_datadir}/kadu/plugins/filedesc.desc
%{_datadir}/kadu/plugins/firewall.desc
%{_datadir}/kadu/plugins/freedesktop_notify.desc
%{_datadir}/kadu/plugins/gadu_protocol.desc
%{_datadir}/kadu/plugins/hints.desc
%{_datadir}/kadu/plugins/history.desc
%{_datadir}/kadu/plugins/idle.desc
%{_datadir}/kadu/plugins/imagelink.desc
%{_datadir}/kadu/plugins/jabber_protocol.desc
%{_datadir}/kadu/plugins/last_seen.desc
%{_datadir}/kadu/plugins/mediaplayer.desc
%{_datadir}/kadu/plugins/mprisplayer_mediaplayer.desc
%{_datadir}/kadu/plugins/pcspeaker.desc
%{_datadir}/kadu/plugins/screenshot.desc
%{_datadir}/kadu/plugins/simpleview.desc
%{_datadir}/kadu/plugins/single_window.desc
%{_datadir}/kadu/plugins/sms.desc
%{_datadir}/kadu/plugins/sound.desc
%{_datadir}/kadu/plugins/speech.desc
%{_datadir}/kadu/plugins/spellchecker.desc
%{_datadir}/kadu/plugins/sql_history.desc
%{_datadir}/kadu/plugins/tabs.desc
%{_datadir}/kadu/plugins/windows_integration.desc
%{_datadir}/kadu/plugins/word_fix.desc
%{_datadir}/kadu/plugins/configuration/antistring.ui
%{_datadir}/kadu/plugins/configuration/autoaway.ui
%{_datadir}/kadu/plugins/configuration/auto_hide.ui
%{_datadir}/kadu/plugins/configuration/autoresponder.ui
%{_datadir}/kadu/plugins/configuration/autostatus.ui
%{_datadir}/kadu/plugins/configuration/cenzor.ui
%{_datadir}/kadu/plugins/configuration/docking.ui
%{_datadir}/kadu/plugins/configuration/docking-notify.ui
%{_datadir}/kadu/plugins/configuration/emoticons.ui
%{_datadir}/kadu/plugins/configuration/ext_sound.ui
%{_datadir}/kadu/plugins/configuration/filedesc.ui
%{_datadir}/kadu/plugins/configuration/firewall.ui
%{_datadir}/kadu/plugins/configuration/freedesktop_notify.ui
%{_datadir}/kadu/plugins/configuration/hints.ui
%{_datadir}/kadu/plugins/configuration/history.ui
%{_datadir}/kadu/plugins/configuration/image-link.ui
%{_datadir}/kadu/plugins/configuration/mediaplayer.ui
%{_datadir}/kadu/plugins/configuration/mprisplayer_mediaplayer.ui
%{_datadir}/kadu/plugins/configuration/screenshot.ui
%{_datadir}/kadu/plugins/configuration/simpleview.ui
%{_datadir}/kadu/plugins/configuration/single_window.ui
%{_datadir}/kadu/plugins/configuration/sms.ui
%{_datadir}/kadu/plugins/configuration/sound.ui
%{_datadir}/kadu/plugins/configuration/speech.ui
%{_datadir}/kadu/plugins/configuration/spellchecker.ui
%{_datadir}/kadu/plugins/configuration/tabs.ui
%{_datadir}/kadu/plugins/configuration/word_fix.ui
%{_datadir}/kadu/plugins/data/antistring/ant_conditions.conf
%{_datadir}/kadu/plugins/data/cenzor/*.conf
%{_datadir}/kadu/plugins/data/mediaplayer/mediaplayer.png
%{_datadir}/kadu/plugins/data/mprisplayer_mediaplayer/mprisplayer-players.data
%{_datadir}/kadu/plugins/data/sms/scripts/gateway*.js
%{_datadir}/kadu/plugins/data/sql_history/scripts/history-database-recovery.sh
%{_datadir}/kadu/plugins/data/word_fix/wf_default_list.data
%{_datadir}/kadu/plugins/translations/antistring_*.qm
%{_datadir}/kadu/plugins/translations/autoaway_*.qm
%{_datadir}/kadu/plugins/translations/auto_hide_*.qm
%{_datadir}/kadu/plugins/translations/autoresponder_*.qm
%{_datadir}/kadu/plugins/translations/autostatus_*.qm
%{_datadir}/kadu/plugins/translations/cenzor_*.qm
%{_datadir}/kadu/plugins/translations/chat_notify_*.qm
%{_datadir}/kadu/plugins/translations/config_wizard_*.qm
%{_datadir}/kadu/plugins/translations/docking_*.qm
%{_datadir}/kadu/plugins/translations/emoticons_*.qm
%{_datadir}/kadu/plugins/translations/encryption_otr_*.qm
%{_datadir}/kadu/plugins/translations/exec_notify_*.qm
%{_datadir}/kadu/plugins/translations/ext_sound_*.qm
%{_datadir}/kadu/plugins/translations/filedesc_*.qm
%{_datadir}/kadu/plugins/translations/firewall_*.qm
%{_datadir}/kadu/plugins/translations/freedesktop_notify_*.qm
%{_datadir}/kadu/plugins/translations/gadu_protocol_*.qm
%{_datadir}/kadu/plugins/translations/hints_*.qm
%{_datadir}/kadu/plugins/translations/history_*.qm
%{_datadir}/kadu/plugins/translations/idle_*.qm
%{_datadir}/kadu/plugins/translations/imagelink_*.qm
%{_datadir}/kadu/plugins/translations/jabber_protocol_*.qm
%{_datadir}/kadu/plugins/translations/last_seen_*.qm
%{_datadir}/kadu/plugins/translations/mediaplayer_*.qm
%{_datadir}/kadu/plugins/translations/mprisplayer_mediaplayer_*.qm
%{_datadir}/kadu/plugins/translations/pcspeaker_*.qm
%{_datadir}/kadu/plugins/translations/screenshot_*.qm
%{_datadir}/kadu/plugins/translations/simpleview_*.qm
%{_datadir}/kadu/plugins/translations/single_window_*.qm
%{_datadir}/kadu/plugins/translations/sms_*.qm
%{_datadir}/kadu/plugins/translations/sound_*.qm
%{_datadir}/kadu/plugins/translations/speech_*.qm
%{_datadir}/kadu/plugins/translations/spellchecker_*.qm
%{_datadir}/kadu/plugins/translations/sql_history_*.qm
%{_datadir}/kadu/plugins/translations/tabs_*.qm
%{_datadir}/kadu/plugins/translations/windows_integration_en.qm
%{_datadir}/kadu/plugins/translations/word_fix_*.qm
%{_datadir}/kadu/qml
%{_datadir}/kadu/scripts/*.js
%{_datadir}/kadu/syntax/chat/*.syntax
%{_datadir}/kadu/syntax/chat/Default
"%{_datadir}/kadu/syntax/chat/Modern Bubbling (Compact)"
%{_datadir}/kadu/syntax/chat/Satin
%{_datadir}/kadu/syntax/chat/SimpleStuff
%{_datadir}/kadu/syntax/chat/Stockholm
%{_datadir}/kadu/syntax/chat/renkooNaked
%{_datadir}/kadu/syntax/chat/ultr
%{_datadir}/kadu/syntax/infopanel/*.syntax
%{_datadir}/kadu/themes/emoticons/penguins/*
%{_datadir}/kadu/themes/emoticons/tango/*
%{_datadir}/kadu/themes/icons/default
%{_datadir}/kadu/themes/icons/faenza
%{_datadir}/kadu/themes/icons/glass
%{_datadir}/kadu/themes/icons/oxygen
%{_datadir}/kadu/themes/sounds/default
%{_datadir}/kadu/translations/*
%{_libdir}/kadu/libkadu.so
%{_libdir}/kadu/plugins/libantistring.so
%{_libdir}/kadu/plugins/libauto_hide.so
%{_libdir}/kadu/plugins/libautoaway.so
%{_libdir}/kadu/plugins/libautoresponder.so
%{_libdir}/kadu/plugins/libautostatus.so
%{_libdir}/kadu/plugins/libcenzor.so
%{_libdir}/kadu/plugins/libchat_notify.so
%{_libdir}/kadu/plugins/libconfig_wizard.so
%{_libdir}/kadu/plugins/libdocking.so
%{_libdir}/kadu/plugins/libdocking_notify.so
%{_libdir}/kadu/plugins/libemoticons.so
%{_libdir}/kadu/plugins/libencryption_otr.so
%{_libdir}/kadu/plugins/libexec_notify.so
%{_libdir}/kadu/plugins/libext_sound.so
%{_libdir}/kadu/plugins/libfiledesc.so
%{_libdir}/kadu/plugins/libfirewall.so
%{_libdir}/kadu/plugins/libfreedesktop_notify.so
%{_libdir}/kadu/plugins/libgadu_protocol.so
%{_libdir}/kadu/plugins/libhints.so
%{_libdir}/kadu/plugins/libhistory.so
%{_libdir}/kadu/plugins/libidle.so
%{_libdir}/kadu/plugins/libimagelink.so
%{_libdir}/kadu/plugins/libjabber_protocol.so
%{_libdir}/kadu/plugins/liblast_seen.so
%{_libdir}/kadu/plugins/libmediaplayer.so
%{_libdir}/kadu/plugins/libmprisplayer_mediaplayer.so
%{_libdir}/kadu/plugins/libpcspeaker.so
%{_libdir}/kadu/plugins/libscreenshot.so
%{_libdir}/kadu/plugins/libsimpleview.so
%{_libdir}/kadu/plugins/libsingle_window.so
%{_libdir}/kadu/plugins/libsms.so
%{_libdir}/kadu/plugins/libsound.so
%{_libdir}/kadu/plugins/libspeech.so
%{_libdir}/kadu/plugins/libspellchecker.so
%{_libdir}/kadu/plugins/libsql_history.so
%{_libdir}/kadu/plugins/libtabs.so
%{_libdir}/kadu/plugins/libwindows_integration.so
%{_libdir}/kadu/plugins/libword_fix.so

%files devel
%defattr(-,root,root)
%dir %{_includedir}/kadu
%{_includedir}/kadu/kadu-core
%{_includedir}/kadu/plugins
%{_datadir}/cmake/Kadu
%{_datadir}/kadu/sdk

### External plugins ###

# %files anonymous_check
# %defattr(-,root,root)
# %{_libdir}/kadu/plugins/libanonymous_check.so
# %{_datadir}/kadu/plugins/anonymous_check.desc
# %{_datadir}/kadu/plugins/translations/anonymous*.qm

# %files completion
# %defattr(-,root,root)
# %dir %{_datadir}/kadu/plugins/data/kadu_completion
# %{_libdir}/kadu/plugins/libkadu_completion.so
# %{_datadir}/kadu/plugins/data/kadu_completion/list.txt
# %{_datadir}/kadu/plugins/kadu_completion.desc

# %files import_history
# %defattr(-,root,root)
# %{_libdir}/kadu/plugins/libimport_history.so
# %{_datadir}/kadu/plugins/import_history.desc
# %{_datadir}/kadu/plugins/translations/import_history*.qm

# %files mimetex
# %defattr(-,root,root)
# %dir %{_datadir}/kadu/plugins/data/mime_tex
# %{_datadir}/kadu/plugins/data/mime_tex/mime_tex_32x32.png
# %dir %{_libdir}/kadu/plugins/bin
# %dir %{_libdir}/kadu/plugins/bin/mime_tex
# %{_libdir}/kadu/plugins/bin/mime_tex/mimetex
# %{_libdir}/kadu/plugins/libmime_tex.so
# %{_datadir}/kadu/plugins/mime_tex.desc
# %{_datadir}/kadu/plugins/configuration/mime_tex.ui
# %{_datadir}/kadu/plugins/translations/mime_tex*.qm
# %dir %{_datadir}/kadu/plugins/data/mime_tex/editor_icons
# %{_datadir}/kadu/plugins/data/mime_tex/editor_icons/*.png
# %dir %{_datadir}/kadu/plugins/data/mime_tex/mime_tex_icons
# %{_datadir}/kadu/plugins/data/mime_tex/mime_tex_icons/*.png

### Emoticons ###
%if %{build_penguins}

%files emoticons_gg6_compatible
%defattr(-,root,root)
%{_datadir}/kadu/themes/emoticons/gg6_compatible

%files emoticons_gg10_compatible
%defattr(-,root,root)
%{_datadir}/kadu/themes/emoticons/gg10_compatible
%endif

### Sounds ###

%files sound-bns
%defattr(-,root,root)
%{_datadir}/kadu/themes/sounds/bns

%files sound-drums
%defattr(-,root,root)
%{_datadir}/kadu/themes/sounds/drums

%files sound-florkus
%defattr(-,root,root)
%{_datadir}/kadu/themes/sounds/florkus

%files sound-michalsrodek
%defattr(-,root,root)
%{_datadir}/kadu/themes/sounds/michalsrodek

%files sound-percussion
%defattr(-,root,root)
%{_datadir}/kadu/themes/sounds/percussion

%files sound-ultr
%defattr(-,root,root)
%{_datadir}/kadu/themes/sounds/ultr

%changelog
