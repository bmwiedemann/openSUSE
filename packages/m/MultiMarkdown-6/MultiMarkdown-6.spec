#
# spec file for package MultiMarkdown-6
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


Name:           MultiMarkdown-6
Version:        6.4.0
Release:        0
Summary:        Reference implementation of MultiMarkdown
License:        MIT
Group:          Productivity/Publishing/Other
URL:            http://fletcherpenney.net/multimarkdown
# We have to use tarball generated via _service as released ones are
# missing submodules that are necessary for building
Source:         %{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  curl-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  texlive-filesystem
Requires:       texlive-filesystem
Requires(post): update-alternatives
Requires(postun): update-alternatives
Conflicts:      MultiMarkdown-5
Provides:       markdown

%description
MultiMarkdown is a derivative of Markdown that adds new syntax features,
such as footnotes, tables, and metadata. Additionally, it offers mechanisms
to convert plain text into LaTeX in addition to HTML.

%prep
%setup -q

%build
%cmake
%make_jobs

%install
%cmake_install
# Avoid conflict with mtools
mv %{buildroot}%{_bindir}/mmd  %{buildroot}%{_bindir}/%{name}-mmd
# multimarkdown is provided by other packages thus we use
# update-alternatives
mv %{buildroot}%{_bindir}/markdown %{buildroot}%{_bindir}/%{name}-markdown
install -d %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/markdown
ln -sf %{_sysconfdir}/alternatives/markdown %{buildroot}%{_bindir}/markdown
%fdupes %{buildroot}

%check
%ctest

%post
update-alternatives \
	--install %{_bindir}/markdown markdown %{_bindir}/%{name}-markdown 40

%postun
if [ ! -f %{_bindir}/%{name}-markdown ] ; then
	update-alternatives --remove markdown %{_bindir}/%{name}-markdown
fi

%files
%license LICENSE.txt
%doc README.md
%ghost %{_sysconfdir}/alternatives/markdown
%{_bindir}/markdown
%{_bindir}/%{name}-markdown
%{_bindir}/%{name}-mmd
%{_bindir}/mmd2all
%{_bindir}/mmd2opml
%{_bindir}/mmd2pdf
%{_bindir}/mmd2tex
%{_bindir}/multimarkdown
%{_bindir}/mmd2epub
%{_bindir}/mmd2fodt
%{_bindir}/mmd2odt
%dir %{_datadir}/texmf/tex/latex/mmd6
%{_datadir}/texmf/tex/latex/mmd6/*

%changelog
