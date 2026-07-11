%global tl_name polski
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.6
Release:	%{tl_revision}.1
Summary:	Typeset Polish documents with LaTeX and Polish fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/polski
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/polski.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/polski.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/polski.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyphen-polish)
Requires:	texlive(pl)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Tools to typeset monolingual Polish documents in LaTeX2e without babel
or polyglossia. The package loads Polish hyphenation patterns, ensures
that a font encoding suitable for Polish is used; in particular it
enables Polish adaptation of Computer Modern fonts (the so-called PL
fonts), provides translations of \today and names like "Bibliography" or
"Chapter", redefines math symbols according to Polish typographical
tradition, provides macros for dashes according to Polish orthography,
provides a historical input method for "Polish characters", works with
traditional TeX as well as with Unicode aware variants. (This package
was previously known as platex, but has been renamed to resolve a name
clash.)

