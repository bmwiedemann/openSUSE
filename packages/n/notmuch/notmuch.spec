#
# spec file for package notmuch
#
# Copyright (c) 2021 SUSE LLC
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


%define libversion 5
Name:           notmuch
Version:        0.32
Release:        0
Summary:        The mail indexer
License:        GPL-3.0-or-later
URL:            https://notmuchmail.org
Source0:        %{URL}/releases/notmuch-%{version}.tar.xz
Source1:        %{URL}/releases/notmuch-%{version}.tar.xz.asc
Source3:        %{URL}/releases/test-databases/database-v1.tar.xz
# key fingerprint: 7A18 807F 100A 4570 C596  8420 7E4E 65C8 720B 706B
Source4:        notmuch.keyring
BuildRequires:  libxapian-devel
# info pages
BuildRequires:  info
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  pkgconfig(gmime-3.0)
BuildRequires:  pkgconfig(talloc)

%{bcond_without python3}
%{bcond_without emacs}

#FIXME: at the moment they are not enabled
%{bcond_with ruby}
%{bcond_with go}

# dtach is not present on SLE
# cannot run the tests there
%if 0%{is_opensuse}
%{bcond_without tests}
%else
%{bcond_with tests}
%endif
# testsuite
%if %{with tests}
BuildRequires:  dtach
BuildRequires:  gdb
BuildRequires:  gnu_parallel
BuildRequires:  libgcrypt-cavs
BuildRequires:  man
BuildRequires:  valgrind-devel
%endif
%if %{with emacs}
BuildRequires:  emacs-el
BuildRequires:  emacs-nox
%endif
%if %{with python3}
BuildRequires:  python3-base
%endif
%if %{with ruby}
BuildRequires:  ruby-devel
%endif
%if %{with go}
BuildRequires:  go
%endif

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
Requires:       libnotmuch%{libversion} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation for %{name}
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains the info pages for %{name}.

%package   -n libnotmuch%{libversion}
Summary:        A shared library for %{name}

%description -n libnotmuch%{libversion}
The libnotmuch3 package contains shared libraries for %{name}.

%if %{with python3}
%package -n python3-%{name}
Summary:        Python3 bindings for %{name}
Requires:       python = %{py3_ver}
Recommends:     python-%{name}-doc = %{version}

%description -n python3-%{name}
Python3 interface (bindings) for %{name}

%package -n python-%{name}-doc
Summary:        Documentation of Python bindings for %{name}

%description -n python-%{name}-doc
Documentation of Python interface (bindings) for %{name}
%endif

%if %{with emacs}
%package emacs
Summary:        Emacs lisp email client based on %{name}
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
export CFLAGS="%{?build_cflags}%{?!build_cflags:%optflags}"
export CXXFLAGS="%{?build_cxxflags}%{?!build_cxxflags:%optflags}"
export LDFLAGS="${RPM_LD_FLAGS}"
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

%{make_build}

#TODO: bindings - go, ruby
pushd bindings

%if %{with python3}
cp -r python python3
pushd python3
python3 setup.py build
pushd docs
%{make_build} dirhtml
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

%check
%if %{with tests}
cp %{SOURCE3} test/test-databases

# this test fails on PPC64 (see id:87o8mpr5w6.fsf@tethera.net)
%ifarch ppc64
export NOTMUCH_SKIP_TESTS="T360-symbol-hiding"
%endif

# can only run the testsuite when debugging symbols are available (boo#1152451)
if echo "%{optflags}"|grep -q '\-g'; then
    %make_build check
fi

%endif
# {with tests}

%post -n libnotmuch%{libversion} -p /sbin/ldconfig
%postun -n libnotmuch%{libversion} -p /sbin/ldconfig

%files
%doc AUTHORS NEWS README
%license COPYING COPYING-GPL-3
%{_bindir}/%{name}
%{_bindir}/%{name}-emacs-mua
%{_mandir}/man1/%{name}*.1%{?ext_man}
%{_mandir}/man5/%{name}-hooks.5%{?ext_man}
%{_mandir}/man7/%{name}-search-terms.7%{?ext_man}
%{_mandir}/man7/%{name}-properties.7%{?ext_man}

%files -n libnotmuch%{libversion}
%{_libdir}/libnotmuch.so.%{libversion}*

%files devel
%{_includedir}/%{name}.h
%{_libdir}/libnotmuch.so

%files doc
%{_infodir}/%{name}.info%{?ext_info}
%{_infodir}/%{name}-*.info%{?ext_info}

%if %{with python3}
%files -n python3-%{name}
%doc bindings/python/README
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*egg-info

%files -n python-%{name}-doc
%doc bindings/python3/docs/build/dirhtml/
%endif

%if %{with emacs}
%files emacs
%{_datadir}/emacs/site-lisp/
%exclude %{_datadir}/applications/
%endif

%changelog
