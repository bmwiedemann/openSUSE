#
# spec file for package python-Twisted
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-Twisted
Version:        21.7.0
Release:        0
Summary:        An asynchronous networking framework written in Python
License:        MIT
URL:            https://twistedmatrix.com/
Source0:        https://files.pythonhosted.org/packages/source/T/Twisted/Twisted-%{version}.tar.gz
Source99:       python-Twisted-rpmlintrc
Patch0:         skip_MultiCast.patch
# PATCH-FIX-UPSTREAM no-test_successResultOfWithFailureHasTraceback.patch https://twistedmatrix.com/trac/ticket/9665 mcepl@suse.com
# skip over the test test_successResultOfWithFailureHasTraceback
Patch2:         no-test_successResultOfWithFailureHasTraceback.patch
# PATCH-FIX-UPSTREAM 1521_delegate_parseqs_stdlib_bpo42967.patch https://twistedmatrix.com/trac/ticket/10096 mcepl@suse.com
# overcome incompatibility with the solution for bpo#42967.
Patch3:         1521_delegate_parseqs_stdlib_bpo42967.patch
# We don't want to package yet another module, and it is easily skippable
Patch4:         no-cython_test_exception_raiser.patch
# boo#1110669 Our variant of PyGObject has pygtkcompat stripped which Twisted does not handle
Patch5:         no-pygtkcompat.patch
# PATCH-FIX-OPENSUSE remove-dependency-version-upper-bounds.patch boo#1190036 -- run with h2 >= 4.0.0 and priority >= 2.0
Patch6:         remove-dependency-version-upper-bounds.patch
# PATCH-FIX-OPENSUSE do not throw DeprecatationWarning, upstream's fix is an API break
Patch7:         currentThread-deprecated.patch
BuildRequires:  %{python_module Automat >= 0.8.0}
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
BuildRequires:  %{python_module incremental >= 21.3.0}
BuildRequires:  %{python_module pyOpenSSL >= 16.0.0}
BuildRequires:  %{python_module pyasn1}
BuildRequires:  %{python_module pyserial >= 3.0}
BuildRequires:  %{python_module pyserial}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-subunit}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module service_identity >= 18.1.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions >= 3.6.5}
BuildRequires:  %{python_module zope.interface >= 4.4.2}
BuildRequires:  fdupes
BuildRequires:  git-core
BuildRequires:  python-rpm-macros
Requires:       python-Automat >= 0.8.0
Requires:       python-PyHamcrest >= 1.9.0
Requires:       python-appdirs >= 1.4.0
Requires:       python-attrs >= 19.2.0
Requires:       python-bcrypt >= 3.0.0
Requires:       python-constantly >= 15.1
Requires:       python-cryptography >= 2.6
Requires:       python-h2 >= 3.0
Requires:       python-hyperlink >= 17.1.1
Requires:       python-idna >= 2.4
Requires:       python-incremental >= 21.3.0
Requires:       python-pyOpenSSL >= 16.0.0
Requires:       python-pyasn1
Requires:       python-pyserial >= 3.0
Requires:       python-service_identity >= 18.1.0
Requires:       python-typing_extensions >= 3.6.5
Requires:       python-zope.interface >= 4.4.2
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
An extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

%package -n %{name}-doc
Summary:        An asynchronous networking framework written in Python - Documentation

%description -n %{name}-doc
An extensible framework for Python programming, with special focus
on event-based network programming and multiprotocol integration.

This package contains the documentation for python-Twisted

%prep
%autosetup -p1 -n Twisted-%{version}
sed -i '1{/env python/d}' src/twisted/mail/test/pop3testserver.py src/twisted/trial/test/scripttest.py

%build
%python_build

%install
%python_install
find %{buildroot} -regex '.*\.[ch]' -exec rm {} ";" # Remove leftover C sources
install -dm0755 %{buildroot}%{_mandir}/man1/
install -m0644 docs/*/man/*.1 %{buildroot}%{_mandir}/man1/ # Install man pages
find docs -type f -print0 | xargs -0 chmod a-x # Fix doc-file dependency by removing x flags
#sed -i "s/\r//" docs/core/howto/listings/udp/{MulticastClient,MulticastServer}.py
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Prepare for update-alternatives usage
for p in twistd cftp ckeygen conch pyhtmlizer tkconch trial ; do
    %python_clone -a %{buildroot}%{_bindir}/$p
    %python_clone -a %{buildroot}%{_mandir}/man1/$p.1
done

# mailmail is useful only on Python 2
rm %{buildroot}%{_bindir}/mailmail %{buildroot}%{_mandir}/man1/mailmail.1

# no manpage for twist yet:
%python_clone -a %{buildroot}%{_bindir}/twist

mkdir -p %{buildroot}%{_docdir}/%{name}-doc
cp -r docs/* %{buildroot}%{_docdir}/%{name}-doc/
# empty files
rm %{buildroot}%{_docdir}/%{name}-doc/{fun/Twisted.Quotes,_static/.placeholder,_templates/.placeholder}
%fdupes %{buildroot}%{_docdir}/%{name}-doc

%check
export LANG=en_US.UTF-8
export PYTHONDONTWRITEBYTECODE=1

%{python_expand # provide flavored commands for testing (=not yet available python_flavored_alternatives from gh#openSUSE/python-rpm-macros#120)
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

%post
# these were master alternatives until Dec 2020. Remove before the install as slave links
for f in cftp ckeygen conch pyhtmlizer tkconch trial twist; do
  (update-alternatives --quiet --list $f 2>&1 >/dev/null) && update-alternatives --quiet --remove-all $f
done
%{python_install_alternative twistd cftp ckeygen conch pyhtmlizer tkconch trial twist
                             twistd.1 cftp.1 ckeygen.1 conch.1 pyhtmlizer.1 tkconch.1 trial.1}

%postun
%python_uninstall_alternative twistd

%files -n %{name}-doc
%doc %{_docdir}/%{name}-doc

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
%{python_sitelib}/twisted
%{python_sitelib}/Twisted-%{version}*-info

%changelog
