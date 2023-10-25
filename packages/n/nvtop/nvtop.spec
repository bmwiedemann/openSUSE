#
# spec file for package nvtop
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020-2023 Malcolm J Lewis <malcolmlewis@opensuse.org>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           nvtop
Version:        3.0.2+31
Release:        0
License:        GPL-3.0-or-later
Summary:        A (h)top like task monitor for NVIDIA and AMD GPUs
URL:            https://github.com/Syllo/nvtop
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(systemd)

%description
Nvtop stands for NVidia TOP, a (h)top like task monitor for AMD, NVIDIA and
now Intel GPUs.

It can handle multiple GPUs and print information about them in a htop familiar
way.

%prep
%autosetup

%build
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DNVML_RETRIEVE_HEADER_ONLINE=True
make %{?_smp_mflags}

%install
%cmake_install
%suse_update_desktop_file %{name}

%files
%license LICENSE
%doc README.markdown
%{_bindir}/nvtop
%{_datadir}/applications/nvtop.desktop
%{_datadir}/icons/nvtop.svg
%{_mandir}/man1/nvtop.1%{?ext_man}
%{_datadir}/metainfo/nvtop.metainfo.xml

%changelog
