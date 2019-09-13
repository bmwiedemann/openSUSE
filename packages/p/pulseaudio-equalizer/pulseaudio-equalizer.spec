#
# spec file for package pulseaudio-equalizer
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           pulseaudio-equalizer
Version:        2.7.0.2
Release:        0
Summary:        PulseAudio's LADSPA plugin graphical user interface
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Mixers
Url:            https://ubuntuforums.org/showthread.php?t=1308838
Source:         https://launchpad.net/~nilarimogard/+archive/ubuntu/webupd8/+files/%{name}_%{version}.orig.tar.gz
# PATCH-FIX-UPSTREAM 0000-add-python3-compat.patch sor.alexei@meowr.ru -- Add Python3 compatibility.
Patch0:         0000-add-python3-compat.patch
# PATCH-FIX-UPSTREAM 0001-pulse-path.patch webupd8@gmail.com -- Update path to PulseAudio files to the new one.
Patch1:         0001-pulse-path.patch
# PATCH-FIX-UPSTREAM 0002-remove-preamp.patch -- Remove preamp.
Patch2:         0002-remove-preamp.patch
# PATCH-FIX-UPSTREAM 0003-force-default-persistence-value.patch webupd8@gmail.com -- Force default persistence value.
Patch3:         0003-force-default-persistence-value.patch
# PATCH-FIX-UPSTREAM 0004-do-not-crash-on-missing-preset.patch webupd8@gmail.com -- Do not crash on missing preset.
Patch4:         0004-do-not-crash-on-missing-preset.patch
# PATCH-FIX-UPSTREAM 0005-window-icon.patch webupd8@gmail.com -- Correct way of setting window icon.
Patch5:         0005-window-icon.patch
# PATCH-FIX-UPSTREAM 0006-fix-desktop.patch malcolmlewis@opensuse.org -- Fix .desktop file.
Patch6:         0006-fix-desktop.patch
# PATCH-FIX-UPSTREAM 0007-pygobject3-port.patch sor.alexei@meowr.ru -- Port to PyGObject3 and GTK+3.
Patch7:         0007-pygobject3-port.patch
# PATCH-FIX-UPSTREAM 0008-fix-locale-issues.patch sor.alexei@meowr.ru -- Fix issues on non-Latin systems.
Patch8:         0008-fix-locale-issues.patch
# PATCH-FIX-UPSTREAM 0009-do-not-zero-volume.patch sor.alexei@meowr.ru -- Fix volume zeroing on fresh PulseAudio.
Patch9:         0009-do-not-zero-volume.patch
BuildRequires:  gobject-introspection-devel
BuildRequires:  update-desktop-files
Requires:       ladspa-swh-plugins
Requires:       pulseaudio >= 4.0
Requires:       pulseaudio-utils >= 4.0
Requires:       python3
Requires:       python3-gobject
BuildArch:      noarch
%if 0%{?suse_version} > 1320 || 0%{?sle_version} >= 120200
Requires:       python3-gobject-Gdk
%endif

%description
GUI for PulseAudio's LADSPA interface using Steve Harris' Multiband EQ
(mbeq_1197) plugin.

%prep
%setup -q -n %{name}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6
%patch7 -p1
%patch8 -p1
%patch9 -p1
sed -i '/^#!/s|env python$|python3|' .%{_datadir}/%{name}/%{name}.py

%build
# Nothing to build.

%install
mkdir -p %{buildroot}%{_bindir}/ %{buildroot}%{_datadir}/%{name}/presets/
install -Dpm 0755 .%{_bindir}/%{name}* %{buildroot}%{_bindir}/
install -Dpm 0755 .%{_datadir}/%{name}/%{name}.py %{buildroot}%{_bindir}/%{name}-gtk
install -Dpm 0644 .%{_datadir}/%{name}/presets/* %{buildroot}%{_datadir}/%{name}/presets/
install -Dpm 0644 .%{_datadir}/applications/%{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%suse_update_desktop_file %{name}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%{_bindir}/%{name}*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop

%changelog
