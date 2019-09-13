#
# spec file for package bash-completion-doc
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           bash-completion-doc
%define _name bash-completion
# WARNING: Never edit this file!!! Edit bash-completion.spec and call pre_checkin.sh to update bash-completion-doc.spec.
# Always set %%build_doc to 0 before submit to OBS.
Version:        2.8
Release:        0
Summary:        The Documentation of Programmable Completion for Bash
License:        GPL-2.0-or-later
Group:          Development/Libraries/C and C++
Url:            https://github.com/scop/bash-completion/
Source0:        https://github.com/scop/bash-completion/releases/download/%{version}/%{_name}-%{version}.tar.xz
Source1:        bash-completion-rpmlintrc
# PATCH-FIX-UPSTREAM bnc#717151 -- Terminal tab autocompletion error
Patch0:         %{_name}-2.4.patch
# PATCH-FIX-SUSE bnc#1012212 -- bash tab-autocompletion hangs on TAR-archiving with --create key
Patch1:         tar-completion.patch
# PATCH-FIX-SUSE bnc#903362 -- tab completion for file names prints error
Patch2:         PS1-completion-boo903362.patch
# PATCH-FIX-SUSE boo#905348 -- tab completion with shell variable changes command line with backslash
Patch3:         FOO-dir-completion-boo905348.patch
# PATCH-FIX-SUSE boo#889319
Patch5:         ls-completion-boo889319.patch
# PATCH-FIX-SUSE boo#940835
Patch6:         backtick-completion-boo940835.patch
# PATCH-FIX-SUSE bsc#946875
Patch7:         LVM-completion-bsc946875.patch
# PATCH-FIX-SUSE boo#940837, bsc#959299
Patch8:         respect-variables-boo940837.patch
# PATCH-FIX-SUSE boo#958462
Patch9:         rm-completion-smart-boo958462.patch
# PATCH-FIX-SUSE boo#963140
Patch10:        backticks-bsc963140.patch
# PATCH-FIX-SUSE boo#977336
Patch11:        sh-script-completion-boo977336.patch
# PATCH-FIX-SUSE boo#1090515
Patch12:        bash-completion-2.7-unRAR-remove.patch
BuildRequires:  asciidoc
BuildRequires:  libxslt-tools
BuildRequires:  pkg-config
Provides:       bash-completion:%{_defaultdocdir}/%{_name}/AUTHORS
BuildArch:      noarch

%description
This package contains the package documentation file of the
package bash-completion.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -b .p0
%patch1 -b .p1
%patch2 -b .p2
%patch3 -b .p3
%patch5 -b .p5
%patch6 -b .p6
%patch7 -b .p7 -p1
%patch8 -b .p8
%patch9 -b .p9
%patch10 -b .p10 -p1
%patch11 -b .p11 -p0
%patch12 -b .p12 -p0

%build
%configure
pushd doc
    mkdir html
    a2x -D html -d book -f xhtml --asciidoc-opts="--unsafe" main.txt
popd

%install
pushd doc
    mkdir -p  %{buildroot}%{_defaultdocdir}/%{_name}/html
    install -m 0644 html/* %{buildroot}%{_defaultdocdir}/%{_name}/html/
popd
install -m 0644 AUTHORS %{buildroot}%{_defaultdocdir}/%{_name}/
install -m 0644 README.md  %{buildroot}%{_defaultdocdir}/%{_name}/README

%files
%defattr(-,root,root)
%dir %{_defaultdocdir}/%{_name}
%{_defaultdocdir}/%{_name}/AUTHORS
%{_defaultdocdir}/%{_name}/README
%{_defaultdocdir}/%{_name}/html/

%changelog
