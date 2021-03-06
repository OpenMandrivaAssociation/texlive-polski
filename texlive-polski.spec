Name:		texlive-polski
Version:	1.3.4
Release:	2
Summary:	Typeset Polish documents with LaTeX and Polish fonts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/polski
License:	LPPL1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polski.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polski.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/polski.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires:	texlive-pl
Requires:	texlive-hyphen-polish

%description
Tools to typeset documents in Polish using LaTeX2e with Polish
fonts (the so-called PL fonts), EC fonts or CM fonts. (This
package was previously known as platex, but has been renamed to
resolve a name clash.).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/polski
%doc %{_texmfdistdir}/doc/latex/polski
#- source
%doc %{_texmfdistdir}/source/latex/polski

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
