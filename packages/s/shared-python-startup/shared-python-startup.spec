#
# spec file for package shared-python-startup
#
# Copyright (c) 2019 SUSE LLC
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


Name:           shared-python-startup
Version:        0.1
Release:        0
Summary:        Startup script shared by all Python interpreters
License:        Python-2.0
Source0:        pythonstart
Source1:        LICENSE
BuildRequires:  filesystem
Supplements:    python(abi)
BuildArch:      noarch

%description
The primary purpose of this package is to share script which can
be run via PYTHONSTARTUP variable of any Python interpreter.

%prep
cp -p %{SOURCE1} .

%build
/bin/true

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/pythonstart
install -D -d -m 755 %{buildroot}%{_sysconfdir}/profile.d

cat > %{buildroot}/%{_sysconfdir}/profile.d/python.sh <<-EOF
# add python startup script for interactive sessions
export PYTHONSTARTUP=%{_sysconfdir}/pythonstart
EOF

cat > %{buildroot}/%{_sysconfdir}/profile.d/python.csh <<-EOF
# add python startup script for interactive sessions
setenv PYTHONSTARTUP %{_sysconfdir}/pythonstart
EOF

%files
%license LICENSE
%config %{_sysconfdir}/pythonstart
%config %{_sysconfdir}/profile.d/python.*sh

%changelog
