#
# spec file for package python-Twisted
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%bcond_without test
%define psuffix -test
%else
%bcond_with test
%define psuffix %{nil}
%endif

%{?sle15_python_module_pythons}
Name:           python-Twisted%{psuffix}
Version:        24.3.0
Release:        0
Summary:        An asynchronous networking framework written in Python
License:        MIT
URL:            https://twisted.org
Source0:        https://files.pythonhosted.org/packages/source/t/twisted/twisted-%{version}.tar.gz
Source99:       python-Twisted.rpmlintrc
Patch0:         skip_MultiCast.patch
# PATCH-FIX-UPSTREAM no-test_successResultOfWithFailureHasTraceback.patch https://twistedmatrix.com/trac/ticket/9665 mcepl@suse.com
# skip over the test test_successResultOfWithFailureHasTraceback
Patch2:         no-test_successResultOfWithFailureHasTraceback.patch
# PATCH-FIX-UPSTREAM 1521_delegate_parseqs_stdlib_bpo42967.patch https://twistedmatrix.com/trac/ticket/10096 mcepl@suse.com
# overcome incompatibility with the solution for bpo#42967.
Patch3:         1521_delegate_parseqs_stdlib_bpo42967.patch
# PATCH-FIX-OPENSUSE We don't want to package yet another module, and it is easily skippable
Patch5:         no-cython_test_exception_raiser.patch
# PATCH-FIX-OPENSUSE remove-dependency-version-upper-bounds.patch boo#1190036 -- run with h2 >= 4.0.0 and priority >= 2.0
Patch6:         remove-dependency-version-upper-bounds.patch
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module incremental >= 21.3.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
# SECTION install requires
Requires:       python-Automat >= 0.8.0
Requires:       python-attrs >= 19.2.0
Requires:       python-constantly >= 15.1
Requires:       python-hyperlink >= 17.1.1
Requires:       python-incremental >= 21.3.0
Requires:       python-typing_extensions >= 3.6.5
Requires:       python-zope.interface >= 4.4.2
# /SECTION
# twisted[tls] is so common, let's keep it tied to the main package for the time being.
Requires:       python-Twisted-tls = %{version}
%if %{with test}
BuildRequires:  %{python_module Twisted-all_non_platform = %{version}}
BuildRequires:  %{python_module Twisted-conch_nacl = %{version}}
# declared nowhere but required to pass 8 tests with timezone checks
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module hypothesis}
%endif
BuildArch:      noarch
%python_subpackages

%description
An extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

%if 0%{?suse_version} > 1500
%package -n %{name}-doc
Summary:        An asynchronous networking framework written in Python - Documentation

%description -n %{name}-doc
An extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

This package contains the documentation for python-Twisted
%endif

%package tls
Summary:        TLS support for Twisted
Requires:       python-Twisted = %{version}
Requires:       python-idna >= 2.4
Requires:       python-pyOpenSSL >= 16.0.0
Requires:       python-service_identity >= 18.1.0

%description tls
Twisted is an extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

This metapackage is for the optional feature tls

%package conch
Summary:        Conch for Twisted
Requires:       python-Twisted = %{version}
Requires:       python-appdirs >= 1.4.0
Requires:       python-bcrypt >= 3.0.0
Requires:       python-cryptography >= 2.6

%description conch
Twisted is an extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

Twisted Conch: The Twisted Shell. Terminal emulation, SSHv2 and telnet.

%package conch_nacl
Summary:        Conch w/ NaCl for Twisted
Requires:       python-Twisted-conch = %{version}

%description conch_nacl
Twisted is an extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

%package serial
Summary:        Serial support for Twisted
Requires:       python-Twisted = %{version}
Requires:       python-pyserial >= 3.0

%description serial
Twisted is an extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

This metapackage is for the optional feature serial

%package http2
Summary:        HTTP/2 support for Twisted
Requires:       python-Twisted = %{version}
Requires:       python-h2 >= 3.0
Requires:       python-priority >= 1.1.0

%description http2
Twisted is an extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

This metapackage is for the optional feature http2

%package contextvars
Summary:        Contextvars extra for Twisted
Requires:       python-Twisted = %{version}

%description contextvars
Twisted is an extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

This metapackage is for the optional dependency contextvars

%package all_non_platform
Summary:        The all_non_platform dependency extra for Twisted
Requires:       python-PyHamcrest >= 1.9.0
Requires:       python-Twisted-conch = %{version}
Requires:       python-Twisted-contextvars = %{version}
Requires:       python-Twisted-http2 = %{version}
Requires:       python-Twisted-serial = %{version}
Requires:       python-Twisted-tls = %{version}

%description all_non_platform
Twisted is an extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

This metapackage is for the optional dependency all_non_platform

%prep
%autosetup -p1 -n twisted-%{version}
sed -i '1{/env python/d}' src/twisted/mail/test/pop3testserver.py src/twisted/trial/test/scripttest.py
find src/twisted -name .gitignore -delete
find src/twisted -name '*.misc' -size 0 -delete

%if ! %{with test}
%build
%pyproject_wheel

# empty files
rm docs/{fun/Twisted.Quotes,_static/.placeholder,_templates/.placeholder}
%fdupes docs
%endif

%if ! %{with test}
%install
%pyproject_install
find %{buildroot} -regex '.*\.[ch]' -exec rm {} ";" # Remove leftover C sources
install -dm0755 %{buildroot}%{_mandir}/man1/
install -m0644 docs/*/man/*.1 %{buildroot}%{_mandir}/man1/ # Install man pages
find docs -type f -print0 | xargs -0 chmod a-x # Fix doc-file dependency by removing x flags
#sed -i "s/\r//" docs/core/howto/listings/udp/{MulticastClient,MulticastServer}.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_docdir}/%{name}-doc
cp -r docs/* %{buildroot}%{_docdir}/%{name}-doc
%fdupes %{buildroot}%{_docdir}/%{name}-doc
%endif

# Prepare for update-alternatives usage
for p in twistd cftp ckeygen conch pyhtmlizer tkconch trial ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
    %python_clone -a %{buildroot}%{_mandir}/man1/$p.1
done

# mailmail is useful only on Python 2
rm %{buildroot}%{_bindir}/mailmail %{buildroot}%{_mandir}/man1/mailmail.1

# no manpage for twist yet:
%python_clone -a %{buildroot}%{_bindir}/twist
%endif

%if %{with test}
%check
export LANG=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1

%{python_expand # provide flavored commands for testing
# (= python_flavored_alternatives from gh#openSUSE/python-rpm-macros#120, but sadly not available for non-TW)
mkdir -p build/bin/
for f in %{buildroot}%{_bindir}/*-%{$python_bin_suffix}; do
  ln -s $f build/bin/$(basename ${f%%%%-%{$python_bin_suffix}})
done
}
export PATH=$PWD/build/bin/:$PATH

# Relax the crypto policies for the test-suite
export OPENSSL_SYSTEM_CIPHERS_OVERRIDE=xyz_nonexistent_file
export OPENSSL_CONF=''

%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python -m twisted.trial twisted
%endif

%post
# these were master alternatives until Dec 2020. Remove before the install as slave links
for f in cftp ckeygen conch pyhtmlizer tkconch trial twist; do
  (update-alternatives --quiet --list $f 2>&1 >/dev/null) && update-alternatives --quiet --remove-all $f
done
%{python_install_alternative twistd cftp ckeygen conch pyhtmlizer tkconch trial twist
                             twistd.1 cftp.1 ckeygen.1 conch.1 pyhtmlizer.1 tkconch.1 trial.1}

%postun
%python_uninstall_alternative twistd

%if ! %{with test}
%files %{python_files tls}
%license LICENSE

%files %{python_files conch}
%license LICENSE

%files %{python_files conch_nacl}
%license LICENSE

%files %{python_files serial}
%license LICENSE

%files %{python_files http2}
%license LICENSE

%files %{python_files contextvars}
%license LICENSE

%files %{python_files all_non_platform}
%license LICENSE

%files %{python_files}
%license LICENSE
%doc NEWS.rst README.rst
%python_alternative %{_bindir}/conch
%python_alternative %{_bindir}/tkconch
%python_alternative %{_mandir}/man1/conch.1%{?ext_man}
%python_alternative %{_mandir}/man1/tkconch.1%{?ext_man}
%python_alternative %{_bindir}/twistd
%python_alternative %{_bindir}/cftp
%python_alternative %{_bindir}/ckeygen
%python_alternative %{_bindir}/pyhtmlizer
%python_alternative %{_bindir}/trial
%python_alternative %{_bindir}/twist
%python_alternative %{_mandir}/man1/twistd.1%{?ext_man}
%python_alternative %{_mandir}/man1/cftp.1%{?ext_man}
%python_alternative %{_mandir}/man1/ckeygen.1%{?ext_man}
%python_alternative %{_mandir}/man1/pyhtmlizer.1%{?ext_man}
%python_alternative %{_mandir}/man1/trial.1%{?ext_man}
%{python_sitelib}/twisted
%{python_sitelib}/twisted-%{version}*-info

%if 0%{?suse_version} > 1500
%files -n %{name}-doc
%doc %{_docdir}/%{name}-doc
%else
%doc docs/
%endif

%endif

%changelog
