#
# spec file for package rubygem-taskjuggler
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
# This file was generated with a gem2rpm.yml and not just plain gem2rpm.
# All sections marked as MANUAL, license headers, summaries and descriptions
# can be maintained in that file. Please consult this file before editing any
# of those fields
#

Name:           rubygem-taskjuggler
Version:        3.6.0
Release:        0
%define mod_name taskjuggler
%define mod_full_name %{mod_name}-%{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  %{ruby >= 2.0.0}
BuildRequires:  %{rubygem gem2rpm}
BuildRequires:  ruby-macros >= 5
BuildRequires:  update-alternatives
Url:            http://www.taskjuggler.org
Source:         http://rubygems.org/gems/%{mod_full_name}.gem
Source1:        gem2rpm.yml
Summary:        A Project Management Software
License:        GPL-2.0
Group:          Development/Languages/Ruby
PreReq:         update-alternatives

%description
TaskJuggler is a modern and powerful, Free and Open Source Software project
management tool. Its new approach to project planing and tracking is more
flexible and superior to the commonly used Gantt chart editing tools.
TaskJuggler is project management software for serious project managers. It
covers the complete spectrum of project management tasks from the first idea
to the completion of the project. It assists you during project scoping,
resource assignment, cost and revenue planing, risk and communication
management.

%prep

%build

%install
%gem_install \
  --symlink-binaries \
  --doc-files="CHANGELOG COPYING README.rdoc" \
  -f
# MANUAL
## vim
# don't turn on folding automatically
sed -i '/foldmethod/d' %{buildroot}%{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}/data/tjp.vim
install -d -m 0755 %{buildroot}%{_datadir}/vim/site/{syntax,ftdetect}
ln -s %{_libdir}/ruby/gems/%{rb_ver}/gems/%{mod_full_name}/data/tjp.vim %{buildroot}%{_datadir}/vim/site/syntax
cat > %{buildroot}%{_datadir}/vim/site/ftdetect/tjp_filetype.vim <<EOF
au BufNewFile,BufRead *.tjp,*.tji  set ft=tjp
EOF
# /MANUAL

%files
%defattr(-,root,root,-)
%{_datadir}/vim

%gem_packages

%changelog
