#
# spec file for package mailprocessing
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mailprocessing
Version:        1.2.6
Release:        0
Summary:        Maildir and IMAP processor/filter using Python 3x as its configuration language
License:        GPL-2.0-only
Group:          Productivity/Networking/Email/Utilities
URL:            http://mailprocessing.github.io/mailprocessing
Source0:        https://github.com/mailprocessing/mailprocessing/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
Requires:       python3
Obsoletes:      maildirproc < %{version}
Provides:       maildirproc = %{version}
BuildArch:      noarch

%description
The maildirproc and imapproc utilities provided by this package filter emails
in maildirs and IMAP folders with a user provided filter script written in
Python.

%prep
%setup -q

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
install -D -m 644 docs/imapproc.1 %{buildroot}/%{_mandir}/man1/imapproc.1
install -D -m 644 docs/maildirproc.1 %{buildroot}/%{_mandir}/man1/maildirproc.1
install -D -m 644 docs/mailprocessing.5 %{buildroot}/%{_mandir}/man5/mailprocessing.5
install -d -m 755 %{buildroot}/%{_docdir}/%{name}
cp -a docs/examples %{buildroot}/%{_docdir}/%{name}
%fdupes %{buildroot}%{$python_sitelib}

%files
%license LICENSE
%doc NEWS README
%doc %{_docdir}/%{name}/examples
%{_mandir}/man1/imapproc.1%{?ext_man}
%{_mandir}/man1/maildirproc.1%{?ext_man}
%{_mandir}/man5/mailprocessing.5%{?ext_man}
%{python3_sitelib}
%{_bindir}/maildirproc
%{_bindir}/imapproc

%changelog
