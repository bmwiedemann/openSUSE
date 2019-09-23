#
# spec file for package picocom
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


Name:           picocom
Version:        3.1
Release:        0
Summary:        Minimal dumb-terminal emulation program
License:        GPL-2.0
Group:          Hardware/Modem
Url:            https://github.com/npat-efault/picocom
Source:         https://github.com/npat-efault/picocom/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
picocom is a dumb-terminal emulation program, similar to "minicom",
for the purpose of manual modem configuration, testing, and
debugging. It can be used as a low-tech "terminal window" to allow
operator intervention in PPP connection scripts (something like the
"open terminal window before / after dialing" feature in MS Windows).

%prep
%setup -q

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_mandir}/man1
install -m 755 %{name} %{buildroot}%{_bindir}/
install -m 644 %{name}.1 %{buildroot}%{_mandir}/man1/

%files
%doc CHANGES.old CONTRIBUTORS LICENSE.txt README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{ext_man}

%changelog
