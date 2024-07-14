from docutils.parsers.rst import roles
from docutils import nodes

def xref_role(role, rawtext, text, lineno, inliner,
                       options=None, content=None):
    sp = text.split(' <')
    if len(sp) != 2:
        msg = inliner.reporter.error(
            'Invalid :xref: role syntex: '
            '%s' % text, line=lineno)
        prb = inliner.problematic(rawtext, rawtext, msg)
        return [prb], [msg]
    t, a = sp
    a = a[:-1].strip()
    node = nodes.reference(t, t, refuri=a, target='_blank',
                           **(options or {}))
    return [node], []

def setup(app):
    app.add_role('xref', xref_role)
