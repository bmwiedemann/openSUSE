#
# spec file for package pamixer
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2017 Dakota Williams <raineforest@raineforest.me>
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


Name:           pamixer
Version:        1.4
Release:        0
Summary:        PulseAudio commandline mixer
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Sound/Mixers
URL:            https://github.com/cdemoulins/pamixer
Source0:        https://github.com/cdemoulins/pamixer/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libboost_program_options-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpulse)

%description
pamixer is like amixer but for PulseAudio. It can control the volume levels
of the sinks.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags}"
%make_build

%install
mkdir -p %{buildroot}%{_bindir}
%make_install PREFIX=%{buildroot}%{_prefix}

%files
%doc README.rst
%license COPYING
%{_bindir}/pamixer

%changelog
