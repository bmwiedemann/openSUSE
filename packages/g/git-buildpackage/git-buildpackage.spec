#
# spec file for package git-buildpackage
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


%bcond_without docs

Name:           git-buildpackage
Summary:        Build packages from git
%if 0%{?mageia}
License:        GPL-2.0-only
Group:          Development/Tools
%else
License:        GPL-2.0-only
Group:          Development/Tools/Building
%endif
Version:        0.9.23
Release:        0
BuildArch:      noarch
URL:            https://honk.sigxcpu.org/piki/projects/git-buildpackage/
Source0:        %{name}-%{version}.tar.gz

# Conditional package names for requirements
%if 0%{?fedora} || 0%{?centos_ver} >= 7 || 0%{?mageia} >= 8
%define dpkg_pkg_name dpkg-dev
%else
%if 0%{?centos_ver}
%define dpkg_pkg_name dpkg-devel
%else
%define dpkg_pkg_name dpkg
%endif
%endif

%if 0%{?fedora} || 0%{?mageia}
%define man_pkg_name man-db
%else
%define man_pkg_name man
%endif

%if 0%{?suse_version}
%define python_pkg_name python3-base
%define rpm_python_pkg_name python3-rpm
# % define do_unittests 1
%define _zipmerge libzip-tools
%else
%if 0%{?mageia}
%define python_pkg_name python3
%define _zipmerge libzip
%define rpm_python_pkg_name python3-rpm
%else
%define _zipmerge /usr/bin/zipmerge
%define python_pkg_name python
%endif
%endif

BuildRequires:  %{dpkg_pkg_name}
Requires:       %{dpkg_pkg_name}
Requires:       %{name}-common = %{version}-%{release}
Requires:       devscripts
BuildRequires:  python3
BuildRequires:  python3-setuptools

%if %{with docs}
%if 0%{?fedora} || 0%{?rhel}
BuildRequires:  docbook2X
BuildRequires:  libxslt
%else
%if 0%{?mageia}
%if 0%{?mageia} >= 8
BuildRequires:  docbook2x
BuildRequires:  libxslt
%else
BuildRequires:  docbook2x
BuildRequires:  libxslt1
%endif
%else
BuildRequires:  docbook2x
BuildRequires:  libxslt-tools
%endif
%endif
BuildRequires:  gtk-doc
%if 0%{?fedora}
BuildRequires:  perl-podlators
%endif
%endif

%if 0%{?do_unittests}
BuildRequires:  %{_zipmerge}
BuildRequires:  %{dpkg_pkg_name}
BuildRequires:  %{man_pkg_name}
BuildRequires:  %{rpm_python_pkg_name}
BuildRequires:  devscripts
BuildRequires:  git-core
BuildRequires:  gnupg
BuildRequires:  pristine-tar
BuildRequires:  python3-coverage
BuildRequires:  python3-mock
BuildRequires:  python3-nose
BuildRequires:  rpm-build
BuildRequires:  unzip
# Missing dep of dpkg in openSUSE
%if 0%{?suse_version}
BuildRequires:  perl-TimeDate
%endif
%endif

%description
Set of tools from Debian that integrate the package build system with Git.
This package contains the original Debian tools.

%package common
Summary:        Common files for git-buildpackage debian and rpm tools
Group:          Development/Tools/Building
Requires:       %{man_pkg_name}
Requires:       %{python_pkg_name}
Requires:       git-core
Requires:       python3-dateutil
Requires:       python3-setuptools
%if 0%{?centos_ver} && 0%{?centos_ver} <= 7
Requires:       %{_zipmerge}
Requires:       unzip
%else
Recommends:     unzip
%if 0%{?suse_version}
Recommends:     %{_zipmerge}
Recommends:     pristine-tar
%endif
%endif

%description common
Common files and documentation, used by both git-buildpackage debian and rpm tools

%package rpm
Summary:        Build RPM packages from git
Group:          Development/Tools/Building
Requires:       %{name}-common = %{version}-%{release}
Requires:       %{rpm_python_pkg_name}
Requires:       rpm
%if 0%{?centos_ver} && 0%{?centos_ver} <= 7
Requires:       rpm-build
%else
Recommends:     rpm-build
%endif

%description rpm
Set of tools from Debian that integrate the package build system with Git.
This package contains the tools for building RPM packages.

%if %{with docs}
%package doc
Summary:        Documentation for the git-buildpackage suite
Group:          Development/Tools/Building

%description doc
This package contains documentation for the git-buildpackage suite - both the
Debian and the RPM tool set.
%endif

%prep
%setup -q -n %{name}-%{version}

%build
WITHOUT_NOSETESTS=1 %{__python3} ./setup.py build

%if %{with docs}
# HTML docs
HAVE_SGML2X=0 make -C docs/
%endif

%if 0%{?do_unittests}
%check
GIT_CEILING_DIRECTORIES=%{_builddir} \
    GIT_AUTHOR_EMAIL=rpmbuild@example.com GIT_AUTHOR_NAME=rpmbuild \
    GIT_COMMITTER_NAME=$GIT_AUTHOR_NAME GIT_COMMITTER_EMAIL=$GIT_AUTHOR_EMAIL \
    %{__python3} setup.py nosetests
%endif

%install
rm -rf %{buildroot}
WITHOUT_NOSETESTS=1 %{__python3} ./setup.py install --root=%{buildroot} --prefix=/usr --install-lib=%{python3_sitelib}
find %{buildroot} -name __pycache__ | xargs rm -r
mkdir -p %{buildroot}/usr/share/%{name}
mv %{buildroot}/usr/bin/gbp-builder-mock %{buildroot}/usr/share/%{name}/
mkdir -p %{buildroot}/%{_sysconfdir}/git-buildpackage/
mv %{buildroot}/usr/share/%{name}/gbp.conf %{buildroot}/%{_sysconfdir}/git-buildpackage/

%if %{with docs}
# Install man pages
install -d  %{buildroot}%{_mandir}/man1 %{buildroot}%{_mandir}/man5
install docs/*.1 %{buildroot}%{_mandir}/man1/
install docs/*.5 %{buildroot}%{_mandir}/man5/

# Install html documentation
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -r docs/manual-html %{buildroot}%{_docdir}/%{name}

# fix perms
chmod -x %{buildroot}%{_mandir}/man1/*.1
chmod -x %{buildroot}%{_mandir}/man5/*.5
chmod -x %{buildroot}%{_docdir}/%{name}/manual-html/images/*.png

%endif

cat > files.list << EOF
%{_bindir}/git-pbuilder
%{python3_sitelib}/gbp/deb
%{python3_sitelib}/gbp/scripts/pq.py*
%{python3_sitelib}/gbp/scripts/buildpackage.py*
%{python3_sitelib}/gbp/scripts/dch.py*
%{python3_sitelib}/gbp/scripts/export_orig.py*
# %{python3_sitelib}/gbp/scripts/export_ref.py*
%{python3_sitelib}/gbp/scripts/import_ref.py*
%{python3_sitelib}/gbp/scripts/import_dsc.py*
%{python3_sitelib}/gbp/scripts/import_dscs.py*
%{python3_sitelib}/gbp/scripts/import_orig.py*
%{python3_sitelib}/gbp/scripts/create_remote_repo.py*
%{python3_sitelib}/gbp/scripts/setup_gitattributes.py*
EOF

%if %{with docs}
cat >> files.list << EOF
%{_mandir}/man1/gbp-buildpackage.1*
%{_mandir}/man1/gbp-create-remote-repo.1*
%{_mandir}/man1/gbp-dch.1*
%{_mandir}/man1/gbp-export-orig.1*
%{_mandir}/man1/gbp-import-dsc.1*
%{_mandir}/man1/gbp-import-dscs.1*
%{_mandir}/man1/gbp-import-orig.1*
%{_mandir}/man1/gbp-import-ref.1*
%{_mandir}/man1/gbp-pq.1*
%{_mandir}/man1/git-pbuilder.1*
%{_mandir}/man1/gbp-setup-gitattributes.1*
EOF
%endif

# Disable the Debian tools for old CentOS
%if 0%{?centos_ver} && 0%{?centos_ver} < 7
for f in `cat files.list`; do
    rm -rfv %{buildroot}/$f
done

%else

%files -f files.list
%defattr(-,root,root,-)
%endif

%files common
%defattr(-,root,root,-)
%{_bindir}/gbp
%dir %{python3_sitelib}/gbp
%dir %{python3_sitelib}/gbp/git
%dir %{python3_sitelib}/gbp/pkg
%dir %{python3_sitelib}/gbp/scripts
%dir %{python3_sitelib}/gbp/scripts/common
%dir /usr/share/git-buildpackage
%{python3_sitelib}/gbp-*
%{python3_sitelib}/gbp/*.py*
%{python3_sitelib}/gbp/scripts/__init__.py*
%{python3_sitelib}/gbp/scripts/clone.py*
%{python3_sitelib}/gbp/scripts/config.py*
%{python3_sitelib}/gbp/scripts/pristine_tar.py*
%{python3_sitelib}/gbp/scripts/pull.py*
%{python3_sitelib}/gbp/scripts/push.py*
%{python3_sitelib}/gbp/scripts/supercommand.py*
%{python3_sitelib}/gbp/scripts/tag.py*
%{python3_sitelib}/gbp/scripts/common/*.py*
%{python3_sitelib}/gbp/git/*.py*
%{python3_sitelib}/gbp/pkg/*.py*
%config %{_sysconfdir}/git-buildpackage

%if 0%{?mageia}
%{python3_sitelib}/gbp/__pycache__/*.pyc
%{python3_sitelib}/gbp/scripts/__pycache__/*.pyc
%{python3_sitelib}/gbp/scripts/common/__pycache__/*.pyc
%{python3_sitelib}/gbp/pkg/__pycache__/*.pyc
%{python3_sitelib}/gbp/git/__pycache__/*.pyc
%endif

%if %{with docs}
%{_mandir}/man1/gbp.1*
%{_mandir}/man1/gbp-clone.1*
%{_mandir}/man1/gbp-config.1*
%{_mandir}/man1/gbp-pristine-tar.1*
%{_mandir}/man1/gbp-pull.1*
%{_mandir}/man1/gbp-push.1*
%{_mandir}/man1/gbp-tag.1*
%{_mandir}/man5/*.5*
%endif

%files rpm
%defattr(-,root,root,-)
%dir %{python3_sitelib}/gbp/rpm
%{python3_sitelib}/gbp/scripts/*rpm*.py*
%{python3_sitelib}/gbp/rpm/*py*
/usr/share/git-buildpackage/gbp-builder-mock
%if %{with docs}
%{_mandir}/man1/gbp-buildpackage-rpm.1*
%{_mandir}/man1/gbp-pq-rpm.1*
%{_mandir}/man1/gbp-import-srpm.1*
%{_mandir}/man1/gbp-rpm-ch.1*
%endif

%if %{with docs}
%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}/
%endif

%changelog
