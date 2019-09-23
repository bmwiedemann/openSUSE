#
# spec file for package viewvc
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


#
%define	apxs	%{_sbindir}/apxs2
%define	apache_libexecdir	%(%{apxs} -q LIBEXECDIR)
%define	apache_sysconfdir	%(%{apxs} -q SYSCONFDIR)
#
%define site_python	%(python -c "import distutils.sysconfig; print distutils.sysconfig.get_python_lib()")
#
%define viewvc_dir /srv/viewvc
Name:           viewvc
Version:        1.1.26
Release:        0
Summary:        Browse a Subversion Repository with a Web Browser
License:        BSD-2-Clause
Group:          Development/Tools/Version Control
Url:            http://www.viewvc.org/
Source0:        http://www.viewvc.org/viewvc-%{version}.tar.gz
Source1:        viewvc.conf
Source99:       viewvc-rpmlintrc
Patch0:         viewvc-buglink.patch
BuildRequires:  apache2-devel
BuildRequires:  python-devel
Requires:       subversion-python
Supplements:    packageand(subversion-server:apache2)
Provides:       subversion-viewcvs = %{version}
Provides:       viewcvs = %{version}
Obsoletes:      subversion-viewcvs < %{version}
Obsoletes:      viewcvs < %{version}
#
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
ViewVC is a browser interface for CVS and Subversion version control
repositories. It generates templatized HTML to present navigable
directory, revision, and change log listings. It can display specific
versions of files as well as diffs between those versions. Basically,
ViewVC provides the bulk of the report-like functionality you expect
out of your version control tool, but much prettier than the average
textual command-line program output.

ViewVC is the successor of ViewCVS.

%prep
%setup -q
%patch0

%build

%install
rm -rf "lib/vclib/ccvs/rcsparse/test-data"
#
mkdir -p %{buildroot}/%{apache_sysconfdir}/conf.d
cp -avL %{SOURCE1} %{buildroot}/%{apache_sysconfdir}/conf.d/viewvc.conf
# viewvc
./viewvc-install --prefix "%{viewvc_dir}" --destdir %{buildroot}
# hack for usage under mod_python
# http://archive.netbsd.se/?ml=viewcvs-users&a=2007-02&t=3231282
# rename /srv/viewcvs/bin/mod_python/viewvc.py to myviewvc.py
# to prevent import cycle with a newer mod_python versions
mv %{buildroot}/srv/viewvc/bin/mod_python/viewvc.py \
   %{buildroot}/srv/viewvc/bin/mod_python/myviewvc.py
#
rm -f %{buildroot}/srv/viewvc/cvsgraph.conf.dist
sed '
s@^#docroot.*@docroot = /viewvc-docroot@
s@^default_root.*@default_root = your_unnamed_project@
s@^cvsgraph_conf.*@cvsgraph_conf = %{viewvc_dir}/cvsgraph.conf@
s@^hr_funout.*@hr_funout = 1@
s@^show_changed_paths.*@show_changed_paths = 0@
/^cvs_roots/,/^$/s/^/###/
/^#svn_roots/,/^$/c\
svn_roots:\
	your_unnamed_project : /srv/svn/repos/<your_unnamed_project> , \
	another_project : /srv/svn/repos/<another_project> \
#
' < conf/viewvc.conf.dist > %{buildroot}%{viewvc_dir}/viewvc.conf
diff -up conf/viewvc.conf.dist %{buildroot}%{viewvc_dir}/viewvc.conf || true
find %{buildroot}%{viewvc_dir} -type d | \
sed "s@%{buildroot}@%dir @" > files.viewvc
find %{buildroot}%{viewvc_dir} -type f | \
sed "s@%{buildroot}@@;/\/templates\/\|\.conf$/s@^@%config (noreplace) @" >> files.viewvc
cat files.viewvc
#

%files -f files.viewvc
%defattr(-,root,root)
%doc LICENSE
%dir %{apache_sysconfdir}/conf.d
%config (noreplace) %{apache_sysconfdir}/conf.d/viewvc.conf

%changelog
