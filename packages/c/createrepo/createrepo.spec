#
# spec file for package createrepo
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


Name:           createrepo
Version:        0.10.4
Release:        0
Summary:        Creates a Common Metadata Repository
License:        GPL-2.0-or-later
Group:          System/Packages
Url:            http://linux.duke.edu/metadata/
Source:         http://createrepo.baseurl.org/download/%{name}-%{version}.tar.gz
Patch1:         createrepo-0.9.9-cache_utime.patch
Patch2:         createrepo-0.9.9-cachefix.patch
Patch3:         createrepo-0.9.9-license-to-confirm.patch
Patch4:         createrepo-0.9.9-sort-packages-before-writing-repodata.patch
Patch5:         createrepo-0.9.9-disable-symlinks.patch
Patch6:         createrepo-0.9.9-by_default_no_database.patch
Patch8:         createrepo-fix_MetaDataGenerator.patch
BuildRequires:  python-devel
Requires:       python-deltarpm
Requires:       python-lxml
Requires:       python-urlgrabber
Requires:       rpm >= 4.1.1
Requires:       rpm-python
Requires:       yum-common >= 3.2.25
Requires:       yum-metadata-parser
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       createrepo-implementation
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This utility generates a common metadata repository from a directory of
RPM packages.

%prep
%setup -q
%patch1
%patch2
%patch3
%patch4 -p1
%patch5
%patch6
%patch8 -p1
sed -i "1d" createrepo/{readMetadata,yumbased,utils,deltarpms,merge}.py # Fix non-executable scripts (remove she-bang line)

%build

%install
# Fix the install paths:
sed -i -e 's|PYLIBDIR = $(PYSYSDIR)/lib/python$(PYVER)|PYLIBDIR = %{py_libdir}|g' \
       -e 's|PKGDIR = $(PYLIBDIR)/site-packages/$(PKGNAME)|PKGDIR = %{python_sitearch}/%{name}|g' \
       createrepo/Makefile
%makeinstall sysconfdir=%{_sysconfdir}
mv %{buildroot}/%{_sysconfdir}/bash_completion.d/createrepo %{buildroot}/%{_sysconfdir}/bash_completion.d/createrepo.sh
for i in genpkgmetadata.py mergerepo mergerepo.py modifyrepo modifyrepo.py ; do rm -f %{buildroot}/%{_sysconfdir}/bash_completion.d/$i ; done

mkdir -p %{buildroot}/%{_sysconfdir}/alternatives
for i in createrepo mergerepo modifyrepo ; do
  mv %{buildroot}/%{_bindir}/$i %{buildroot}/%{_bindir}/${i}_yum
  ln -s %{_bindir}/${i}_yum %{buildroot}/%{_sysconfdir}/alternatives/$i
  ln -s %{_sysconfdir}/alternatives/$i %{buildroot}/%{_bindir}/$i
done
for i in mergerepo modifyrepo ; do
  mv %{buildroot}/%{_mandir}/man1/$i.1 %{buildroot}/%{_mandir}/man1/${i}_yum.1
  ln -s %{_mandir}/man1/${i}_yum.1.gz %{buildroot}/%{_sysconfdir}/alternatives/$i.1.gz
  ln -s %{_sysconfdir}/alternatives/$i.1.gz %{buildroot}/%{_mandir}/man1/$i.1.gz
done
for i in createrepo ; do
  mv %{buildroot}/%{_mandir}/man8/$i.8 %{buildroot}/%{_mandir}/man8/${i}_yum.8
  ln -s %{_mandir}/man8/${i}_yum.8.gz %{buildroot}/%{_sysconfdir}/alternatives/$i.8.gz
  ln -s %{_sysconfdir}/alternatives/$i.8.gz %{buildroot}/%{_mandir}/man8/$i.8.gz
done

%post
update-alternatives \
  --install %{_bindir}/createrepo createrepo %{_bindir}/createrepo_yum 15 \
  --slave %{_bindir}/mergerepo mergerepo %{_bindir}/mergerepo_yum \
  --slave %{_bindir}/modifyrepo modifyrepo %{_bindir}/modifyrepo_yum \
  --slave %{_mandir}/man8/createrepo.8.gz createrepo.8.gz %{_mandir}/man8/createrepo_yum.8.gz \
  --slave %{_mandir}/man1/mergerepo.1.gz mergerepo.1.gz %{_mandir}/man1/mergerepo_yum.1.gz \
  --slave %{_mandir}/man1/modifyrepo.1.gz modifyrepo.1.gz %{_mandir}/man1/modifyrepo_yum.1.gz

%postun
if test ! -f %{_bindir}/createrepo_yum ; then
  update-alternatives --remove createrepo %{_bindir}/createrepo_yum
fi

%files
%defattr(-,root,root)
%license COPYING COPYING.lib
%doc ChangeLog README
%{_bindir}/*
%{_mandir}/*/*
%config %{_sysconfdir}/bash_completion.d/createrepo.sh
%{_datadir}/%{name}/
%{python_sitearch}/*
%ghost %{_sysconfdir}/alternatives/*

%changelog
