#
# spec file for package reptyr
#
# Copyright (c) 2020 SUSE LLC
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


Name:           reptyr
Version:        0.8.0
Release:        0
Summary:        A tool for "re-ptying" programs
License:        MIT
Group:          System/Console
URL:            https://github.com/nelhage/reptyr
Source:         https://github.com/nelhage/reptyr/archive/%{name}-%{version}.tar.gz
BuildRequires:  bash-completion
BuildRequires:  gcc

%description
reptyr is a utility for taking an existing running program and
attaching it to a new terminal. Started a long-running process over
ssh, but have to leave and don't want to interrupt it? Just start a
screen, use reptyr to grab it, and then kill the ssh session and head
on home.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%make_build

%install
%make_install PREFIX="%{_prefix}" BASHCOMPDIR="%{_datadir}/bash-completion/completions"

%files
%doc ChangeLog README.md NOTES
%license COPYING
%{_mandir}/man1/reptyr.1%{?ext_man}
%{_mandir}/fr/man1/reptyr.1%{?ext_man}
%{_bindir}/reptyr
%{_datadir}/bash-completion/completions/reptyr

%changelog
