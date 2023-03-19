#
# spec file for package ctags
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


Name:           ctags
Version:        5.8
Release:        0
Summary:        A Program to Generate Tag Files for Use with vi and Other Editors
License:        GPL-2.0-or-later
Group:          Development/Tools/Navigators
URL:            http://ctags.sourceforge.net/
Source0:        http://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/%{name}-%{version}.tar.gz
# No resources to make this patch work with ctags-5.8 (applied to ctags-5.7)
# Anyone is welcome to make it work again.
Source2:        ctags-ycp-parser.diff
Patch1:         0001-Mixing-with-anjuta-tags-https-git.gnome.org-browse-a.patch
Patch2:         0002-Making-inline-behave-like-an-attribute.-Fixes-1.patch
Patch3:         0003-Treat-typename-as-an-attribute.patch
Patch4:         0004-parseReturnType-should-start-from-the-first-non-brac.patch
Patch5:         0005-Ensuring-a-space-is-printed-in-return-type-AFTER-the.patch
Patch6:         0006-Prevent-C-static_assert-from-stopping-parsing.patch
Patch7:         0007-c-Handle-C-11-noexcept.patch
Patch8:         0008-c-Properly-parse-C-11-override-and-final-members.patch
Patch9:         0009-Parse-C-11-enums-with-type-specifier.patch
Patch10:        0010-Parse-C-11-classed-enums.patch
Patch11:        0011-Handle-template-expressions-that-may-use-the-or-oper.patch
Patch12:        0012-Make-sure-we-don-t-throw-things-away-while-collectin.patch
Patch13:        0013-C-mitigate-matching-error-on-generics-containing-an-.patch
Patch14:        0014-fix-wrongly-interpreted-in-template.patch
Patch15:        0015-Added-constexpr-as-keyword.patch
Patch16:        0016-CVE-2014-7204.patch
Patch17:        0017-Go-language-support.patch
Patch18:        0018-SUSE-man-page-changes.patch
Patch19:        0019-Do-not-include-build-time-in-binary.patch
Patch20:        ctags-gcc11.patch
Patch21:        CVE-2022-4515.patch
BuildRequires:  update-alternatives
Requires(pre):  update-alternatives
Requires(post): update-alternatives
Requires(post): coreutils
Provides:       arduino-ctags

%description
CTags (from Darren Hiebert) generates tag files from source code in C,
C++, Eiffel, Fortran, and Java to be used with vi and its derivatives,
Emacs, and several other editors.

%prep
%setup -q
%autopatch -p1

%build
%configure
%make_build

%install
# Makefile ignores DESTDIR ...
%make_install \
  prefix=%{buildroot}%{_prefix} \
  bindir=%{buildroot}%{_bindir} \
  mandir=%{buildroot}%{_mandir}

mv %{buildroot}%{_bindir}/ctags{,-exuberant}
mv %{buildroot}%{_mandir}/man1/ctags{,-exuberant}.1

mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
ln -s %{_sysconfdir}/alternatives/ctags              %{buildroot}%{_bindir}/ctags
ln -s %{_sysconfdir}/alternatives/ctags.1%{ext_man}  %{buildroot}%{_mandir}/man1/ctags.1%{ext_man}

%post
test -L %{_bindir}/ctags || rm -f %{_bindir}/ctags
update-alternatives --install %{_bindir}/ctags ctags %{_bindir}/ctags-exuberant 20 \
  --slave %{_mandir}/man1/ctags.1.gz ctags.1 %{_mandir}/man1/ctags-exuberant.1.gz

%postun
if [ ! -f %{_bindir}/ctags-exuberant ]; then
  update-alternatives --remove ctags %{_bindir}/ctags-exuberant
fi

%files
%license COPYING
%doc EXTENDING.html FAQ README
%{_bindir}/ctags
%{_bindir}/ctags-exuberant
%{_mandir}/man1/ctags-exuberant.1%{ext_man}
%{_mandir}/man1/ctags.1%{ext_man}
%ghost %{_sysconfdir}/alternatives/ctags
%ghost %{_sysconfdir}/alternatives/ctags.1%{ext_man}

%changelog
