#
# spec file for package fastfetch
#
# Copyright (c) 2024 SUSE LLC
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


Name:           fastfetch
Version:        2.16.0
Release:        0
Summary:        Neofetch-like tool written mostly in C
License:        MIT
URL:            https://github.com/fastfetch-cli/fastfetch
Source:         https://github.com/fastfetch-cli/fastfetch/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  Mesa-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  opencl-headers
BuildRequires:  vulkan-headers
# For some reason these don't build on Leap
%if 0%{?suse_version} > 1600
%ifarch %{ix86} x86_64
BuildRequires:  pkgconfig(DirectX-Headers)
%endif
%endif
BuildRequires:  pkgconfig(ImageMagick)
BuildRequires:  pkgconfig(chafa)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libxfconf-0)
BuildRequires:  pkgconfig(ocl-icd)
BuildRequires:  pkgconfig(rpm)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(vulkan)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xrandr)
BuildRequires:  pkgconfig(zlib)
Recommends:     ImageMagick
Recommends:     Mesa
Recommends:     chafa
Recommends:     dbus-1
Recommends:     dconf
Recommends:     glib2-tools
Recommends:     pciutils
Recommends:     rpm
Recommends:     sqlite3
Recommends:     vulkan-tools
Recommends:     xfconf
Recommends:     xrandr
Recommends:     zlib

%description
Fastfetch is a neofetch-like tool for fetching system information and
displaying them in a pretty way.  It is written mainly in C, with performance and
customizability in mind. Currently Linux, Android, FreeBSD,
MacOS and Windows 7+ are supported.

%package        fish-completion
Summary:        Fish Completion for %{name}
Supplements:    (%{name} and fish)
Requires:       fish
BuildArch:      noarch

%description    fish-completion
Fish command-line completion support for %{name}.

%package        bash-completion
Summary:        Bash Completion for %{name}
Supplements:    (%{name} and bash-completion)
Requires:       bash-completion
BuildArch:      noarch

%description    bash-completion
Bash command-line completion support for %{name}.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md CHANGELOG.md
%{_bindir}/flashfetch
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_datadir}/%{name}/

%files bash-completion
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/fastfetch

%files fish-completion
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/fastfetch.fish

%changelog
