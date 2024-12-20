#
# spec file for package picocom
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


%define realversion 2024-07
Name:           picocom
Version:        2024.07
Release:        0
Summary:        Minimal dumb-terminal emulation program
License:        BSD-2-Clause AND GPL-2.0-or-later
Group:          Hardware/Modem
URL:            https://gitlab.com/wsakernel/picocom/
Source:         https://gitlab.com/wsakernel/picocom/-/archive/%{realversion}/%{name}-%{realversion}.tar.bz2
BuildRequires:  go-md2man
Provides:       bundled(linenoise) = 1.0

%description
picocom is a dumb-terminal emulation program, similar to "minicom",
for the purpose of manual modem configuration, testing, and
debugging. It can be used as a low-tech "terminal window" to allow
operator intervention in PPP connection scripts (something like the
"open terminal window before / after dialing" feature in MS Windows).

%package bash-completion
Summary:        Bash Completion for %{name}
Group:          Hardware/Modem
Requires:       %{name} = %{version}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)
BuildArch:      noarch

%description bash-completion
Bash completion script for %{name}.

%prep
%setup -q -n %{name}-%{realversion}

%build
%make_build CFLAGS="%{optflags}"
%make_build doc

%install
install -Dpm 755 picocom %{buildroot}%{_bindir}/picocom
install -Dpm 644 picocom.1 %{buildroot}%{_mandir}/man1/picocom.1
install -Dpm 644 bash_completion/picocom %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%license LICENSE.txt
%doc README.md
%{_bindir}/picocom
%{_mandir}/man1/picocom.1%{?ext_man}

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
