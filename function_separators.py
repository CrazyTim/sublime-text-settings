import sublime
import sublime_plugin
from Default import comment

class FunctionSeparatorListener(sublime_plugin.ViewEventListener):
    @classmethod
    def is_applicable(cls, settings):
        # no way to tell if the scope is `source` or `text` at this point, so just ignore Plain Text files...
        syntax = settings.get('syntax')
        return not syntax or not syntax.startswith('Packages/Plain Text/')

    phantomset = None
    def __init__(self, view):
        super().__init__(view)
        self.phantomset = sublime.PhantomSet(view)
        #self.on_modified_async()


    # dfsdf
    def on_modified_async(self):

        regions = self.view.find_by_selector('entity.name.function')

        # base64 single pixel image
        #img = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mOMDLD/DwAD2wHpIYLm3AAAAABJRU5ErkJggg==' # brown
        img = 'iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mPkiUr9DwADEQHM4Xg5IgAAAABJRU5ErkJggg==' # blue
        
        width = 700
        
        # if rulers are defined, use the last ruler position instead
        rulers = self.view.settings().get('rulers', [])
        if len(rulers) > 0:
            width = self.view.em_width() * rulers[-1]

        # loop through each region
        phantoms = []
        for region in regions:
            new_region = sublime.Region(self.view.text_point(self.view.rowcol(region.begin())[0]-1, 0))

            #begin_line_above = sublime.Region(self.view.text_point(max(0, self.view.rowcol(region.begin())[0] - 1), 0)) # if it is the first line in the file, just put the line under the function name

            # put the horizontal separator line above doc comments
            #while begin_line_above.begin() > 0 and self.view.match_selector(comment.advance_to_first_non_white_space_on_line(self.view, begin_line_above.begin()), 'comment.block.documentation, comment.line.documentation'):
            #    begin_line_above = self.view.line(begin_line_above.begin() - 1)
            # add the phantom
            phantoms.append(sublime.Phantom(new_region, '<img width="{}px" style="margin-top:200px" src="data:image/png;base64,{}" height="1px" />'.format(width, img), sublime.LAYOUT_BLOCK))
        
        self.phantomset.update(phantoms)

    def on_activated_async(self):
        self.on_modified_async()
