import mistune
from mistune import Renderer
renderer = Renderer(escape=True, hard_wrap=True)
markdown = mistune.Markdown(renderer=renderer)
markdown('I am using **mistune markdown parser**')