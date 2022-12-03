import ui
import keyboard

layout1 = '`1234567890qwertyuiopasdfghjklzxcvbnm,.'
layout2 = '⋄¨¯<≤=≥>≠∨∧ ⍵∊⍴~↑↓⍳○*⍺⌈⌊_∇∆∘\'⎕⊂⊃∩∪⊥⊤|⍪⍠'
layout3 = '⍬!@#$%^&*() /\\⌿⍀←→{}⍞×÷≡≢⌹\'"[]-+⍎⍕⊣⊢;:?'
layout1s = '~1234567890QWERTYUIOPASDFGHJKLZXCVBNM!?'
layout2s = '⌺⌶⍫⍒⍋⌽⍉⊖⍟⍱⍲ ⍹⍷⍴⍨←→⍸⍥⍣⍶⌈⌊⍛⍢⍙⍤⌸⌷⊆⊇∩∪⊣⊢∥⍝⍠'

layout1 = "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./"
layout1s = "~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>?"
layout2 = "˜˘¨⁼⌜´˝ ∞¯•÷×⌽𝕨∊↑∧ ⊔⊏⊐π←→ ⍉𝕤↕𝕗𝕘⊸∘○⟜⋄↩⥊𝕩↓∨⌊ ≡∾≍≠"
layout2s = "¬⎉⚇⍟◶⊘⎊⍎⍕⟨⟩√⋆↙𝕎⍷𝕣⍋  ⊑⊒⍳⊣⊢ ↖𝕊 𝔽𝔾« ⌾»·˙⋈𝕏 ⍒⌈ ≢≤≥⇐"

layoutNames = ['ABC', '⊑⎉𝕩']
keybg = '#8c7052'
brdbg = '#232323'
tint = '#ffffff'
shftkey = ['⇧', '⇪']


class BQNKeyboardView(ui.View):

    def __init__(self, *a, **kw):
        super().__init__(*a, **kw)
        self.background_color = brdbg
        self.tint_color = tint

        self.shift = False
        self.shiftLock = False
        self.layouts = [[layout1, layout2], [layout1s, layout2s]]
        self.layout = 0
        self.layoutTrans = [[1, 0], [1, 0]]

    def did_load(self):
        self.setKeyLayout()

        for i in range(len(layout1)):
            self[f'b{i}'].action = self.out_action
            self[f'b{i}'].background_color = keybg

        #self['space'].action = self.out_action

        for side in 'lr':
            self[f'shft{side}'].action = self.shft_action
            self[f'alt{side}'].action = self.alt_action
            self[f'shft{side}'].background_color = keybg
            self[f'alt{side}'].background_color = keybg

        self['go'].action = self.go_action
        self['go'].background_color = keybg
        #self['bksp'].action = self.bksp_action
        #self['down'].action = self.down_action

    def setKeyLayout(self):
        shft = 1 if (self.shiftLock or self.shift) else 0
        layout = self.layouts[shft][self.layout]
        for i in range(len(layout1)):
            title = layout[i]
            if self.layout == 1:
                title += "\ufe0e"
            self[f'b{i}'].title = title
            self.setAltLabels()
        for side in 'lr':
            self[f'shft{side}'].title = shftkey[self.shiftLock]

    def out_action(self, sender):
        text = sender.title[0]
        self.shift = False
        self.setKeyLayout()
        if keyboard.is_keyboard():
            keyboard.play_input_click()
            keyboard.insert_text(text)
        else:
            print('Keyboard input:', text)

    def bksp_action(self, sender):
        keyboard.backspace(times=1)

    def shft_action(self, sender):
        if self.shift:
            if not self.shiftLock:
                self.shiftLock = True
            else:
                self.shiftLock = self.shift = False
        elif self.shiftLock:
            self.shiftLock = False
        else:
            self.shift = True

        self.setKeyLayout()

    def down_action(self, sender):
        pass

    def go_action(self, sender):
        text = '\n'
        if keyboard.is_keyboard():
            keyboard.play_input_click()
            keyboard.insert_text(text)
        else:
            print('Keyboard input:', text)

    def alt_action(self, sender):
        side = 0 if sender.name[-1] == 'r' else 1
        trans = self.layoutTrans
        self.layout = trans[side][self.layout]

        # reset shift state when changing layouts
        self.shift = False
        self.shiftLock = False
        self.setKeyLayout()

    def setAltLabels(self):
        nxtr, nxtl = list(zip(*self.layoutTrans))[self.layout]
        self['altl'].title = layoutNames[nxtl]
        self['altr'].title = layoutNames[nxtr]


def main():
    #v = CharsView(frame = (0, 0, 320, 40))
    #if keyboard.is_keyboard():
    #	keyboard.set_view(v, 'current')
    v = ui.load_view('BQNKeyboard.pyui')
    if keyboard.is_keyboard():
        keyboard.set_view(v, 'expanded')
    else:
        # For debugging in the main app:
        v.name = 'BQNKeyboardView'
        v.present('sheet')


if __name__ == '__main__':
    main()
