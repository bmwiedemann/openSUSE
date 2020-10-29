#
# spec file for package python-Twisted
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define modname Twisted
%define skip_python2 1
Name:           python-Twisted
Version:        20.3.0
Release:        0
Summary:        An asynchronous networking framework written in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://twistedmatrix.com/
Source:         https://files.pythonhosted.org/packages/source/T/Twisted/%{modname}-%{version}.tar.bz2
Patch1:         skip_MultiCast.patch
Patch2:         no-pygtkcompat.patch
Patch3:         test-mktime-invalid-tm_isdst.patch
Patch5:         python-38-hmac-digestmod.patch
Patch6:         python-38-no-cgi-parseqs.patch
Patch7:         true-binary.patch
# PATCH-FIX-UPSTREAM no-test_successResultOfWithFailureHasTraceback.patch https://twistedmatrix.com/trac/ticket/9665 mcepl@suse.com
# skip over the test test_successResultOfWithFailureHasTraceback
Patch8:         no-test_successResultOfWithFailureHasTraceback.patch
BuildRequires:  %{python_module Automat >= 0.3.0}
BuildRequires:  %{python_module PyHamcrest >= 1.9.0}
BuildRequires:  %{python_module appdirs >= 1.4.0}
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module bcrypt >= 3.0.0}
BuildRequires:  %{python_module constantly >= 15.1}
BuildRequires:  %{python_module cryptography >= 2.6}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module h2 >= 3.0}
BuildRequires:  %{python_module hyperlink >= 17.1.1}
BuildRequires:  %{python_module idna >= 2.4}
BuildRequires:  %{python_module incremental >= 16.10.1}
BuildRequires:  %{python_module pyOpenSSL >= 16.0.0}
BuildRequires:  %{python_module pyasn1}
BuildRequires:  %{python_module pyserial >= 3.0}
BuildRequires:  %{python_module pyserial}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module service_identity >= 18.1.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module zope.interface >= 4.4.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Automat >= 0.3.0
Requires:       python-PyHamcrest >= 1.9.0
Requires:       python-appdirs >= 1.4.0
Requires:       python-attrs >= 19.2.0
Requires:       python-bcrypt >= 3.0.0
Requires:       python-constantly >= 15.1
Requires:       python-cryptography >= 2.6
Requires:       python-h2 >= 3.0
Requires:       python-hyperlink >= 17.1.1
Requires:       python-idna >= 2.4
Requires:       python-incremental >= 16.10.1
Requires:       python-pyOpenSSL >= 16.0.0
Requires:       python-pyasn1
Requires:       python-pyserial >= 3.0
Requires:       python-service_identity >= 18.1.0
Requires:       python-zope.interface >= 4.4.2
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
An extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

%package -n %{name}-doc
Summary:        An asynchronous networking framework written in Python - Documentation
Group:          Development/Languages/Python

%description -n %{name}-doc
An extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

This package contains the documentation for python-Twisted

%prep
%setup -q -n %{modname}-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
find %{buildroot} -regex '.*\.[ch]' -exec rm {} ";" # Remove leftover C sources
install -dm0755 %{buildroot}%{_mandir}/man1/
install -m0644 docs/*/man/*.1 %{buildroot}%{_mandir}/man1/ # Install man pages
find docs -type f -print0 | xargs -0 chmod a-x # Fix doc-file dependency by removing x flags
#sed -i "s/\r//" docs/core/howto/listings/udp/{MulticastClient,MulticastServer}.py
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# Prepare for update-alternatives usage
for p in twistd cftp ckeygen conch pyhtmlizer tkconch trial ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
    %python_clone -a %{buildroot}%{_mandir}/man1/$p.1
done

# mailmail is useful only on Python 2
rm %{buildroot}%{_bindir}/mailmail %{buildroot}%{_mandir}/man1/mailmail.1

# no manpage for twist yet:
%python_clone -a %{buildroot}%{_bindir}/twist

%check
export LANG=en_US.UTF-8
export PATH=%{buildroot}%{_bindir}:$PATH
export PYTHONDONTWRITEBYTECODE=1
%python_expand PYTHONPATH=%{buildroot}%{$python_sitearch} $python -m twisted.trial twisted

%post
%python_install_alternative twist
%python_install_alternative trial
%python_install_alternative tkconch
%python_install_alternative pyhtmlizer
%python_install_alternative conch
%python_install_alternative ckeygen
%python_install_alternative cftp
%python_install_alternative twistd

%postun
%python_uninstall_alternative twist
%python_uninstall_alternative trial trial.1
%python_uninstall_alternative tkconch tkconch.1
%python_uninstall_alternative pyhtmlizer pyhtmlizer.1
%python_uninstall_alternative conch conch.1
%python_uninstall_alternative ckeygen ckeygen.1
%python_uninstall_alternative cftp cftp.1
%python_uninstall_alternative twistd twistd.1

%files -n %{name}-doc
%doc docs/*

%files %{python_files}
%license LICENSE
%doc NEWS.rst README.rst
%python_alternative %{_bindir}/twistd
%python_alternative %{_bindir}/cftp
%python_alternative %{_bindir}/ckeygen
%python_alternative %{_bindir}/conch
%python_alternative %{_bindir}/pyhtmlizer
%python_alternative %{_bindir}/tkconch
%python_alternative %{_bindir}/trial
%python_alternative %{_bindir}/twist
%python_alternative %{_mandir}/man1/twistd.1%{?ext_man}
%python_alternative %{_mandir}/man1/cftp.1%{?ext_man}
%python_alternative %{_mandir}/man1/ckeygen.1%{?ext_man}
%python_alternative %{_mandir}/man1/conch.1%{?ext_man}
%python_alternative %{_mandir}/man1/pyhtmlizer.1%{?ext_man}
%python_alternative %{_mandir}/man1/tkconch.1%{?ext_man}
%python_alternative %{_mandir}/man1/trial.1%{?ext_man}
%{python_sitearch}/*

%changelog
