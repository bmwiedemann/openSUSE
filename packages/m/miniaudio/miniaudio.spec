#
# spec file for package miniaudio
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           miniaudio
Version:        0.11.24
Release:        0
Summary:        Audio playback and capture library written in C, in a single source file
License:        MIT-0 OR Unlicense
URL:            https://github.com/mackron/miniaudio
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

%description
%{summary}.

%package devel
Summary:        Headerfile for %{name}
BuildArch:      noarch

%description devel
%{summary}.

%prep
%autosetup

%build
# nothing to build here, as it's only a header file

%install
install -t %{buildroot}%{_includedir}/%{name} -Dpm0644 %{name}.h

%check
# The package does include tests but they are interactive so we cannot use them

%files devel
%license LICENSE
%doc CONTRIBUTING.md README.md
%{_includedir}/%{name}

%changelog
