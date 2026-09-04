from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.statemachine import StringList
from sphinx.application import Sphinx


class PassThroughOptions(dict):
    def __contains__(self, key):
        return True

    def __getitem__(self, key):
        if key in ("no-latex-header", "hide-initializer"):
            return directives.flag
        return directives.unchanged


class LatexTocDoxygenBase(Directive):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = True
    option_spec = PassThroughOptions()
    doxy_type: str

    def run(self):
        name = self.arguments[0]
        escaped_name = name.replace("_", r"\_")
        no_latex = "no-latex-header" in self.options
        toclevel = self.options.get("toclevel", "subsubsection")
        hide_initializer = "hide-initializer" in self.options

        rst = []
        if not no_latex:
            rst.extend(
                [
                    ".. raw:: latex",
                    "",
                    "    \\phantomsection",
                    f"    \\addcontentsline{{toc}}{{{toclevel}}}{{{escaped_name}}}",
                    "",
                ]
            )

        rst.append(f".. {self.doxy_type}:: {name}")

        for k, v in self.options.items():
            if k not in ("no-latex-header", "toclevel", "hide-initializer"):
                rst.append(f"   :{k}:" if v is None else f"   :{k}: {v}")

        if self.content:
            rst.append("")
            rst.extend(f"   {line}" for line in self.content)

        node = nodes.Element()
        env = self.state.document.settings.env

        orig_initializer_setting = getattr(
            env.config, "breathe_show_define_initializer", False
        )

        if hide_initializer:
            env.config.breathe_show_define_initializer = False

        try:
            self.state.nested_parse(
                StringList(rst, source=self.state.document.current_source),
                self.content_offset,
                node,
            )
        finally:
            if hide_initializer:
                env.config.breathe_show_define_initializer = orig_initializer_setting

        return node.children


class LatexTocDoxygenFunction(LatexTocDoxygenBase):
    doxy_type = "doxygenfunction"


class LatexTocDoxygenStruct(LatexTocDoxygenBase):
    doxy_type = "doxygenstruct"


class LatexTocDoxygenDefine(LatexTocDoxygenBase):
    doxy_type = "doxygendefine"


class LatexTocDoxygenTypedef(LatexTocDoxygenBase):
    doxy_type = "doxygentypedef"


def setup(app: Sphinx):
    app.add_directive("latex-toc-doxygenfunction", LatexTocDoxygenFunction)
    app.add_directive("latex-toc-doxygenstruct", LatexTocDoxygenStruct)
    app.add_directive("latex-toc-doxygendefine", LatexTocDoxygenDefine)
    app.add_directive("latex-toc-doxygentypedef", LatexTocDoxygenTypedef)
    return {"version": "1.0", "parallel_read_safe": True}
