import sublime
import sublime_plugin

class NewTabsAreMarkdown(sublime_plugin.EventListener):
   def on_new(self, view):
      view.set_syntax_file('Packages/MarkdownEditing/Markdown.sublime-syntax')
