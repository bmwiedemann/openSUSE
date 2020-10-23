#
# spec file for package rpmlint
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


Name:           rpmlint
Version:        1.11
Release:        0
Summary:        RPM file correctness checker
License:        GPL-2.0-or-later
Group:          System/Packages
URL:            https://github.com/rpm-software-management/rpmlint
Source0:        https://github.com/rpm-software-management/rpmlint/archive/rpmlint-%{version}.tar.gz
Source1:        rpmlint-checks-master.tar.xz
Source2:        config
Source11:       pie.config
Source12:       licenses.config
Source99:       README.packaging.txt
Source100:      syntax-validator.py
Patch00:        rpmlint-suse.diff
Patch01:        suse-checks.diff
Patch02:        suse-version.diff
Patch03:        suse-url-check.diff
Patch04:        suse-python3-naming-policy.diff
Patch05:        suse-tests-without-badness.patch
Patch06:        suse-pkg-config-check.diff
Patch07:        suse-binarieschecks.diff
Patch08:        no-doc-for-lib.diff
Patch09:        suse-filter-exception.diff
Patch10:        suse-spdx-license-exceptions.patch
Patch11:        suse-skip-macro-expansion.diff
Patch23:        suse-filter-more-verbose.diff
Patch24:        docdata-examples.diff
Patch25:        yast-provides.diff
Patch29:        rpmgroup-checks.diff
Patch30:        devel-provide-is-devel-package.diff
Patch31:        only-reg-files-are-scripts.diff
Patch32:        0001-ZipCheck-Also-ignore-RuntimeError.patch
Patch40:        no-badness-return.diff
Patch41:        suse-shlib-devel-dependency.diff
Patch49:        extend-suse-conffiles-check.diff
Patch51:        suse-speccheck-utf8.diff
Patch54:        suse-ignore-specfile-errors.diff
Patch55:        invalid-filerequires.diff
Patch57:        check-for-self-provides.diff
Patch58:        remove-ghostfile-checks.diff
Patch63:        fix-diag-sortorder.diff
Patch72:        rpmlint-slpp-NUM-NUM.patch
Patch77:        suse-rpmlint-all-pie.patch
Patch78:        add-check-for-a-non-zero-.text-segment-in-.a-archive.patch
Patch79:        rpm415-workaround.diff
BuildRequires:  desktop-file-utils
BuildRequires:  obs-service-format_spec_file
BuildRequires:  python3-flake8
BuildRequires:  python3-magic
BuildRequires:  python3-pytest
BuildRequires:  python3-rpm
BuildRequires:  xz
#!BuildIgnore:  rpmlint-mini
Requires:       %{_bindir}/readelf
Requires:       bash
Requires:       checkbashisms
Requires:       cpio
Requires:       dash
Requires:       desktop-file-utils
Requires:       file
Requires:       findutils
Requires:       python3-magic
Requires:       python3-pybeam
Requires:       python3-rpm
Requires:       python3-xml
BuildArch:      noarch

%description
rpmlint is a tool to check common errors on RPM packages. Binary and
source packages can be checked.

%prep
%autosetup -n rpmlint-rpmlint-%{version} -a1 -p1

cp -p %{SOURCE2} .
chmod a-x rpmlint-checks-master/*.py
# Only move top-level python files
mv rpmlint-checks-master/*.py .

%build
%make_build PYTHON=%{_bindir}/python3

%install
%make_install PYTHON=%{_bindir}/python3
# the provided bash-completion does not work and only prints bash errors
rm -rf  %{buildroot}%{_sysconfdir}/bash_completion.d
mv %{buildroot}%{_sysconfdir}/rpmlint/config %{buildroot}%{_datadir}/rpmlint/config
head -n 8 %{buildroot}%{_datadir}/rpmlint/config > %{buildroot}%{_sysconfdir}/rpmlint/config
# make sure that the package is sane
for f in %{buildroot}%{_datadir}/rpmlint/*.py %{buildroot}%{_datadir}/rpmlint/config; do
    echo $f
    env LC_ALL=C.utf8 python3 -tt %{SOURCE100} $f
done
install -m 644 %{SOURCE11} %{buildroot}/%{_sysconfdir}/rpmlint/

cp %{SOURCE12} licenses.config
# note there is a tab character behind the -d, so don't copy&paste lightly
cut '-d	' -f1 %{_prefix}/lib/obs/service/format_spec_file.files/licenses_changes.txt | tail -n +2 | sort -u | while read l; do
  sed -i -e "s/\(#VALIDLICENSES\)/\1\n	'$l',/" licenses.config
done
# add some deprecated licenses we allow for now
for l in AGPL-3.0 AGPL-3.0+ GFDL-1.1 GFDL-1.1+ GFDL-1.2 GFDL-1.2+ GFDL-1.3 GFDL-1.3+ GPL-3.0-with-GCC-exception \
   GPL-2.0-with-classpath-exception GPL-2.0-with-font-exception SUSE-LGPL-2.1+-with-GCC-exception SUSE-NonFree \
   GPL-1.0+ GPL-1.0 GPL-2.0+ GPL-2.0 GPL-3.0+ GPL-3.0 LGPL-2.0 LGPL-2.0+ LGPL-2.1+ LGPL-2.1 LGPL-3.0+ LGPL-3.0; do
  sed -i -e "s/\(#VALIDLICENSES\)/\1\n  '$l',/" licenses.config
done
install -m 644  licenses.config %{buildroot}/%{_sysconfdir}/rpmlint/

%check
env PYTHON=%{_bindir}/python3 ./test.sh

%files
%license COPYING
%doc README*
%{_bindir}/rpmlint
%{_bindir}/rpmdiff
%{_datadir}/rpmlint
%config(noreplace) %{_sysconfdir}/rpmlint/config
%config %{_sysconfdir}/rpmlint/pie.config
%config %{_sysconfdir}/rpmlint/licenses.config
%dir %{_sysconfdir}/rpmlint
%{_mandir}/man1/rpmlint.1%{?ext_man}
%{_mandir}/man1/rpmdiff.1%{?ext_man}

%changelog
