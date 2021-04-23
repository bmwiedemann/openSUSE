#
# spec file for package jack_capture
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2005 JackLab, Germany.
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


Name:           jack_capture
Version:        0.9.73
Release:        0
Summary:        A small program to jack
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/Sound/Utilities
URL:            https://github.com/kmatheussen/jack_capture
Source0:        https://github.com/kmatheussen/jack_capture/archive/%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libsndfile-devel
BuildRequires:  pkgconfig
%if %{defined fedora}
BuildRequires:  jack-audio-connection-kit-devel
%else
BuildRequires:  libjack-devel
%endif

%description
jack_capture is a small program to capture whatever
sound is going out to your speakers into a file.

%prep
%setup -q

%build
export CXXFLAGS="%{optflags}"
%make_build

%install

install -dm 755 %{buildroot}%{_bindir}
install -s -m 755 %{name} %{buildroot}%{_bindir}

%files
%doc README
%{_bindir}/%{name}

%changelog
