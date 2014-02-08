# revision 19881
# category Package
# catalog-ctan /macros/latex/contrib/polski
# catalog-date 2010-09-24 16:10:39 +0200
# catalog-license lppl1.2
# catalog-version 1.3.3
Name:		texlive-polski
Version:	1.3.3
Release:	3
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
%{_texmfdistdir}/tex/latex/polski/amigapl.def
%{_texmfdistdir}/tex/latex/polski/mazovia.def
%{_texmfdistdir}/tex/latex/polski/omlplcm.fd
%{_texmfdistdir}/tex/latex/polski/omlplm.fd
%{_texmfdistdir}/tex/latex/polski/omsplsy.fd
%{_texmfdistdir}/tex/latex/polski/omxplex.fd
%{_texmfdistdir}/tex/latex/polski/ot1patch.sty
%{_texmfdistdir}/tex/latex/polski/ot4ccr.fd
%{_texmfdistdir}/tex/latex/polski/ot4cmdh.fd
%{_texmfdistdir}/tex/latex/polski/ot4cmfib.fd
%{_texmfdistdir}/tex/latex/polski/ot4cmfr.fd
%{_texmfdistdir}/tex/latex/polski/ot4cmr.fd
%{_texmfdistdir}/tex/latex/polski/ot4cmss.fd
%{_texmfdistdir}/tex/latex/polski/ot4cmtt.fd
%{_texmfdistdir}/tex/latex/polski/plprefix.sty
%{_texmfdistdir}/tex/latex/polski/polski.sty
%{_texmfdistdir}/tex/latex/polski/qxenc.def
%doc %{_texmfdistdir}/doc/latex/polski/conowego.txt
%doc %{_texmfdistdir}/doc/latex/polski/czytaj.txt
%doc %{_texmfdistdir}/doc/latex/polski/polski.pdf
%doc %{_texmfdistdir}/doc/latex/polski/readme.txt
%doc %{_texmfdistdir}/doc/latex/polski/sample-polski.tex
%doc %{_texmfdistdir}/doc/latex/polski/sample-rysunek.mp
%doc %{_texmfdistdir}/doc/latex/polski/sample-rysunek1.mps
#- source
%doc %{_texmfdistdir}/source/latex/polski/ot1patch.dtx
%doc %{_texmfdistdir}/source/latex/polski/ot1patch.ins
%doc %{_texmfdistdir}/source/latex/polski/plfonts.fdd
%doc %{_texmfdistdir}/source/latex/polski/plprefix.dtx
%doc %{_texmfdistdir}/source/latex/polski/plprefix.ins
%doc %{_texmfdistdir}/source/latex/polski/polski.dtx
%doc %{_texmfdistdir}/source/latex/polski/polski.ins
%doc %{_texmfdistdir}/source/latex/polski/strony.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3.3-2
+ Revision: 754986
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3.3-1
+ Revision: 719281
- texlive-polski
- texlive-polski
- texlive-polski
- texlive-polski

