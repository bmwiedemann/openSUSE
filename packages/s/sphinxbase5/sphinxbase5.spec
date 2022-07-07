#
# spec file for package sphinxbase5
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


%define sover 3
Name:           sphinxbase5
Version:        5~git20220609.617e536
Release:        0
Summary:        Support library required by Pocketsphinx
License:        BSD-2-Clause AND MIT
Group:          Productivity/Office/Other
URL:            http://cmusphinx.sourceforge.net/wiki/download/
Source:         sphinxbase-%{version}.tar.xz
# PATCH-FIX-UPSTREAM initialize some variables before usage
Patch0:         sphinxbase-initialize-vars.patch
BuildRequires:  alsa-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  lapack-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-Cython
BuildRequires:  python3-devel
BuildRequires:  swig
Requires(post): update-alternatives
Requires(postun):update-alternatives

%description
CMU Sphinx toolkit is a speech recognition tool and has a number of packages for
different tasks and applications.

%package -n libsphinxbase%{sover}
Summary:        Sphinxbase speech recognizer library
Group:          System/Libraries

%description -n libsphinxbase%{sover}
CMU Sphinx toolkit is a speech recognition tool and has a number of packages for
different tasks and applications.

%package devel
Summary:        Headers for support library required by Pocketsphinx
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       alsa-devel
Requires:       lapack-devel
Requires:       libsndfile-devel
Requires:       libsphinxbase%{sover} = %{version}
Conflicts:      sphinxbase-devel

%description devel
devel files for %{name}-%{version}

CMU Sphinx toolkit is a speech recognition tool and has a number of packages for
different tasks and applications.

%package -n python3-sphinxbase5
Summary:        Python bindings for sphinxbase required by python-pocketsphinx
Group:          Development/Languages/Python
Requires:       %{name} = %{version}
Conflicts:      python3-pocketsphinx-python <= 0.1.3
Conflicts:      python3-sphinxbase

%description -n python3-sphinxbase5
Python3 bindings for %{name}-%{version}

CMU Sphinx toolkit is a speech recognition tool and has a number of packages for
different tasks and applications.

%prep
%setup -q -n sphinxbase-%{version}
%patch0

%build
./autogen.sh
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}

# Prepare for alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
for binary in sphinx_cepview sphinx_fe sphinx_jsgf2fsg \
              sphinx_lm_convert sphinx_lm_eval sphinx_pitch ; do
    mv %{buildroot}%{_bindir}/$binary %{buildroot}%{_bindir}/$binary-%{version}
    ln -s %{_sysconfdir}/alternatives/$binary %{buildroot}%{_bindir}/$binary
done

%check
make check

%post
update-alternatives --install %{_bindir}/sphinx_pitch sphinx_pitch %{_bindir}/sphinx_pitch-%{version} 20 \
  --slave %{_bindir}/sphinx_cepview sphinx_cepview %{_bindir}/sphinx_cepview-%{version} \
  --slave %{_bindir}/sphinx_fe sphinx_fe %{_bindir}/sphinx_fe-%{version} \
  --slave %{_bindir}/sphinx_jsgf2fsg sphinx_jsgf2fsg %{_bindir}/sphinx_jsgf2fsg-%{version} \
  --slave %{_bindir}/sphinx_lm_convert sphinx_lm_convert %{_bindir}/sphinx_lm_convert-%{version} \
  --slave %{_bindir}/sphinx_lm_eval sphinx_lm_eval %{_bindir}/sphinx_lm_eval-%{version} \

%postun
if [ ! -f %{_bindir}/sphinx_pitch ]; then
    update-alternatives --remove sphinx_pitch %{_bindir}/sphinx_pitch-%{version}
fi

%post   -n libsphinxbase%{sover} -p /sbin/ldconfig
%postun -n libsphinxbase%{sover} -p /sbin/ldconfig

%files
%doc AUTHORS README NEWS
%license LICENSE
%ghost %{_sysconfdir}/alternatives/sphinx_cepview
%ghost %{_sysconfdir}/alternatives/sphinx_fe
%ghost %{_sysconfdir}/alternatives/sphinx_jsgf2fsg
%ghost %{_sysconfdir}/alternatives/sphinx_lm_convert
%ghost %{_sysconfdir}/alternatives/sphinx_lm_eval
%ghost %{_sysconfdir}/alternatives/sphinx_pitch
%{_bindir}/sphinx_cepview*
%{_bindir}/sphinx_fe*
%{_bindir}/sphinx_jsgf2fsg*
%{_bindir}/sphinx_lm_convert*
%{_bindir}/sphinx_lm_eval*
%{_bindir}/sphinx_pitch*
%{_bindir}/sphinx_cont_seg
%{_mandir}/man1/sphinx_*.1*

%files -n libsphinxbase%{sover}
%{_libdir}/*.so.%{sover}*

%files devel
%{_libdir}/*.so
%{_libdir}/pkgconfig/sphinxbase.pc
%{_includedir}/sphinxbase/
%{_datadir}/sphinxbase/

%files -n python3-sphinxbase5
%{python3_sitearch}/sphinxbase/

%changelog
