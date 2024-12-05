#
# spec file for package harec
#
# Copyright (c) 2023 SUSE LLC
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

%define  haredir  %{_usrsrc}/hare
Name:           madeline
Release:        0
Version:        0.1+git.1716356019.c693a0a
Summary:        Hare readline
URL:            https://git.sr.ht/~ecs/madeline
Source0:        %{name}-%{version}.tar.zst
Source99:       madeline-rpmlintrc
BuildRequires:  hare
BuildRequires:  zstd
BuildArch:      noarch
License:        GPL-3.0-only

%description
tiny readline-alike with some batteries included

%prep
%autosetup -p1

%build
:

%install
install -dm755 %{buildroot}%{haredir}/third-party
cp -avt %{buildroot}%{haredir}/third-party graph made

%check
hare test

%files
%license LICENSE README
%dir %{haredir}
%{haredir}/third-party

%changelog
