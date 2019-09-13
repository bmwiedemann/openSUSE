#
# spec file for package pocketsphinx
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


Name:           pocketsphinx
Version:        0.8
Release:        0
Summary:        Speech recognizer library written in C
License:        BSD-2-Clause
Group:          Productivity/Office/Other
Url:            http://cmusphinx.sourceforge.net/wiki/download/
Source:         http://downloads.sourceforge.net/project/cmusphinx/pocketsphinx/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pocketsphinx-doxygen.patch -- Obtained from fedora package (http://pkgs.fedoraproject.org/cgit/rpms/pocketsphinx.git/tree/)
Patch0:         pocketsphinx-doxygen.patch
# PATCH-FIX-UPSTREAM pocketsphinx-largefile.patch -- Obtained from fedora package (http://pkgs.fedoraproject.org/cgit/rpms/pocketsphinx.git/tree/)
Patch1:         pocketsphinx-largefile.patch
# PATCH-FIX-UPSTREAM pocketsphinx-long-utterance.patch -- Obtained from fedora package (http://pkgs.fedoraproject.org/cgit/rpms/pocketsphinx.git/tree/)
Patch2:         pocketsphinx-long-utterance.patch
BuildRequires:  alsa-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gstreamer-devel
BuildRequires:  pkgconfig
BuildRequires:  python-Cython
BuildRequires:  python-devel
BuildRequires:  python-gtk-devel
BuildRequires:  sphinxbase-devel
Requires(post): update-alternatives
Requires(postun): update-alternatives

%description
Pocketsphinx is a version of the open-source CMU Sphinx II speech
recognition system which is able to recognize speech in real-time.

%package -n libpocketsphinx1
Summary:        Speech recognizer library
Group:          System/Libraries

%description -n libpocketsphinx1
CMU Sphinx toolkit has a number of packages for different tasks and
applications. Pocketsphinx is a version of the open-source CMU Sphinx
II speech recognition system which is able to recognize speech in
real-time.

%package devel
Summary:        Development files for pocketsphinx, a speech recognizer library
Group:          Development/Libraries/C and C++
Requires:       libpocketsphinx1 = %{version}

%description devel
CMU Sphinx toolkit has a number of packages for different tasks and
applications. Pocketsphinx is a version of the open-source CMU Sphinx
II speech recognition system which is able to recognize speech in
real-time.

This is the development package for pocketsphinx.

%package -n python2-pocketsphinx
Summary:        Python bindings for pocketsphinx
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description -n python2-pocketsphinx
Pocketsphinx is a version of the open-source CMU Sphinx II speech
recognition system which is able to recognize speech in real-time.

This package provides python bindings for pocketsphinx.

%prep
%setup -q
%patch0
%patch1
%patch2
rm python/pocketsphinx.c

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
%fdupes %{buildroot}
find %{buildroot} -type f -name "*.la" -delete -print

# Prepare for alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
for binary in pocketsphinx_batch pocketsphinx_continuous pocketsphinx_mdef_convert ; do
    mv %{buildroot}%{_bindir}/$binary %{buildroot}%{_bindir}/$binary-%{version}
    ln -s %{_sysconfdir}/alternatives/$binary %{buildroot}%{_bindir}/$binary
done

%check
make check

%post
update-alternatives --install %{_bindir}/pocketsphinx_batch pocketsphinx_batch %{_bindir}/pocketsphinx_batch-%{version} 10 \
  --slave %{_bindir}/pocketsphinx_continuous pocketsphinx_continuous %{_bindir}/pocketsphinx_continuous-%{version} \
  --slave %{_bindir}/pocketsphinx_mdef_convert pocketsphinx_mdef_convert %{_bindir}/pocketsphinx_mdef_convert-%{version}

%postun
if [ ! -f %{_bindir}/pocketsphinx_batch ]; then
    update-alternatives --remove pocketsphinx_batch %{_bindir}/pocketsphinx_batch-%{version}
fi

%post   -n libpocketsphinx1 -p /sbin/ldconfig
%postun -n libpocketsphinx1 -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog README
%license COPYING
%ghost %{_sysconfdir}/alternatives/pocketsphinx_batch
%ghost %{_sysconfdir}/alternatives/pocketsphinx_continuous
%ghost %{_sysconfdir}/alternatives/pocketsphinx_mdef_convert
%{_bindir}/pocketsphinx_batch*
%{_bindir}/pocketsphinx_continuous*
%{_bindir}/pocketsphinx_mdef_convert*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/model
%{_datadir}/%{name}/model/hmm
%{_datadir}/%{name}/model/lm
%{_mandir}/man1/*%{ext_man}

%files -n libpocketsphinx1
%{_libdir}/*.so.*

%files devel
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/pocketsphinx.pc

%files -n python2-pocketsphinx
%{py_sitedir}/*.so
%{py_sitedir}/PocketSphinx-%{version}-py2.7.egg-info

%changelog
