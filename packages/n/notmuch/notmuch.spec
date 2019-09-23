#
# spec file for package notmuch
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


Name:           notmuch
Version:        0.29.1
Release:        0
Summary:        The mail indexer
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Email/Utilities
Url:            https://notmuchmail.org
Source0:        https://notmuchmail.org/releases/notmuch-%{version}.tar.xz
Source1:        https://notmuchmail.org/releases/notmuch-%{version}.tar.xz.asc
Source3:        https://notmuchmail.org/releases/test-databases/database-v1.tar.xz
Source4:        notmuch.keyring

%{bcond_without python}
%{bcond_without python3}
%{bcond_without emacs}

#FIXME: at the moment they are not enabled
%{bcond_with ruby}
%{bcond_with go}

# dtach is not present on Leap 42 or SLE <= 12
# cannot run the tests there
%if 0%{?suse_version} == 1315
%{bcond_with tests}
%else
%{bcond_without tests}
%endif

%define libversion 5

BuildRequires:  libxapian-devel
BuildRequires:  pkg-config
BuildRequires:  python3-Sphinx
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  pkgconfig(talloc)
# info pages
BuildRequires:  makeinfo
Requires(post): %{install_info_prereq}
Requires(preun):%{install_info_prereq}

# testsuite
%if %{with tests}
BuildRequires:  dtach
BuildRequires:  gdb
BuildRequires:  libgcrypt-cavs
BuildRequires:  man
BuildRequires:  valgrind-devel
%endif # {with tests}

%if %{with emacs}
BuildRequires:  emacs-el
BuildRequires:  emacs-nox
%endif
%if %{with python}
BuildRequires:  python-devel
%endif
%if %{with python3}
BuildRequires:  python3-devel
%endif
%if %{with ruby}
BuildRequires:  ruby-devel
%endif
%if %{with go}
BuildRequires:  go
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Because dealing with your mail can be so much better.

"Not much mail" is what Notmuch thinks about your email collection. Even if
you receive 12000 messages per month or have on the order of millions of
messages that you've been saving for decades. Regardless, Notmuch will be
able to quickly search all of it. It's just plain not much mail.

"Not much mail" is also what you should have in your inbox at any time.
Notmuch gives you what you need, (tags and fast search), so that you can
keep your inbox tamed and focus on what really matters in your life, (which
is surely not email).

Notmuch is an answer to Sup. Sup is a very good email program written by
William Morgan (and others) and is the direct inspiration for Notmuch.
Notmuch began as an effort to rewrite performance-critical pieces of Sup in
C rather than ruby. From there, it grew into a separate project. One
significant contribution Notmuch makes compared to Sup is the separation of
the indexer/searcher from the user interface. (Notmuch provides a library
interface so that its indexing/searching/tagging features can be integrated
into any email program.)

Notmuch is not much of an email program. It doesn't receive messages (no
POP or IMAP support). It doesn't send messages (no mail composer, no
network code at all). And for what it does do (email search) that work is
provided by an external library, Xapian. So if Notmuch provides no user
interface and Xapian does all the heavy lifting, then what's left here? Not
much.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libnotmuch%{libversion} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Group:          Documentation/Man
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains the info pages for %{name}.


%package   -n libnotmuch%{libversion}
Summary:        A shared library for %{name}
Group:          Productivity/Networking/Email/Utilities

%description -n libnotmuch%{libversion}
The libnotmuch3 package contains shared libraries for %{name}.

%if %{with python}
%package -n python-%{name}
Summary:        Python bindings for %{name}
#py_requires is useless as it was not designed for sub-packages
#BR: python-devel is on the top of spec file
Group:          Development/Libraries/Python
Requires:       python = %{py_ver}
Recommends:     python-%{name}-doc = %{version}

%description -n python-%{name}
Python interface (bindings) for %{name}

%package -n python-%{name}-doc
Summary:        Documentation of Python bindings for %{name}
Group:          Documentation/HTML

%description -n python-%{name}-doc
Documentation of Python interface (bindings) for %{name}
%endif

%if %{with python3}
%package -n python3-%{name}
Summary:        Python3 bindings for %{name}
Group:          Development/Libraries/Python
Requires:       python = %{py3_ver}
%if %{with python}
#documentation is built only when python2 is installed
#this shall be fixed once python2 disappear from openSUSE
Recommends:     python-%{name}-doc = %{version}
%endif

%description -n python3-%{name}
Python3 interface (bindings) for %{name}
%endif

%if %{with emacs}
%package emacs
Summary:        Emacs lisp email client based on %{name}
Group:          Productivity/Networking/Email/Utilities
Requires:       %{name} = %{version}-%{release}
Requires:       emacs
Requires:       emacs-el

%description emacs
%{name}-based email client written in emacs lisp
%endif

%prep
%autosetup

%build
#hand-made configure script
#zsh completion is a part of zsh itself
export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
./configure \
%if %{without emacs}
  --without-emacs \
%endif
  --prefix=%{_prefix} \
  --sysconfdir=%{_sysconfdir} \
  --datadir=%{_datadir} \
  --includedir=%{_includedir} \
  --libdir=%{_libdir} \
  --libexecdir=%{_libexecdir} \
  --localstatedir=%{_localstatedir} \
  --mandir=%{_mandir} \
  --infodir=%{_infodir} \
  --disable-dependency-tracking \
  --without-zsh-completion

%{?make_build}
%{?!make_build: make}

#TODO: bindings - go, ruby
pushd bindings

%if %{with python3}
cp -r python python3
pushd python3
python3 setup.py build
popd
%endif

%if %{with python}
pushd python
python2 setup.py build
pushd docs
make dirhtml
rm -f build/dirhtml/.buildinfo
popd
popd
%endif

popd

%install
%make_install

%if %{with python3}
pushd bindings/python3
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
popd
%endif

%if %{with python}
pushd bindings/python
python2 setup.py install --prefix=%{_prefix} --root=%{buildroot}
popd
%endif

%check
%if %{with tests}
cp %{SOURCE3} test/test-databases

# this test fails on PPC64 & PPC64LE
# upstream knows about that
%ifarch %power64
export NOTMUCH_SKIP_TESTS="T360-symbol-hiding"
%endif # power64
# FIXME: why does this test fail only on armv7l?
%ifarch %arm
export NOTMUCH_SKIP_TESTS="T600-named-queries"
%endif # arm

# FIXME: T357-index-decryption throws std::bad_alloc on Leap 15.0 & 15.1
%if 0%{?sle_version} >= 150000 && 0%{?is_opensuse}
export NOTMUCH_SKIP_TESTS="T357-index-decryption ${NOTMUCH_SKIP_TESTS}"
%endif # Leap 15.x

make check
%endif # {with tests}

%post -n libnotmuch%{libversion} -p /sbin/ldconfig
%postun -n libnotmuch%{libversion} -p /sbin/ldconfig

%post doc
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun doc
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%files
%doc AUTHORS NEWS README
%license COPYING COPYING-GPL-3
%{_bindir}/%{name}
%{_bindir}/%{name}-emacs-mua
%{_mandir}/man1/%{name}*.1*
%{_mandir}/man5/%{name}-hooks.5*
%{_mandir}/man7/%{name}-search-terms.7*
%{_mandir}/man7/%{name}-properties.7*

%files -n libnotmuch%{libversion}
%{_libdir}/libnotmuch.so.%{libversion}*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/libnotmuch.so

%files doc
%{_infodir}/%{name}.info.*
%{_infodir}/%{name}-*.info.*

%if %{with python}
%files -n python-%{name}
%doc bindings/python/README
%{python_sitelib}/%{name}/
%{python_sitelib}/%{name}*egg-info

%files -n python-%{name}-doc
%doc bindings/python/docs/build/dirhtml/
%endif

%if %{with python3}
%files -n python3-%{name}
%doc bindings/python/README
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*egg-info
%endif

%if %{with emacs}
%files emacs
%{_datadir}/emacs/site-lisp/
%exclude %{_datadir}/applications/
%endif

%changelog
