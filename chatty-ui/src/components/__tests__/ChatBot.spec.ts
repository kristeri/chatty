import { describe, it, expect } from 'vitest'

import { mount } from '@vue/test-utils'
import ChatBot from '../ChatBot.vue'

describe('ChatBot', () => {
  it('renders properly', () => {
    const wrapper = mount(ChatBot, { props: { msg: 'Hello Vitest' } })
    expect(wrapper.text()).toContain('Hello Vitest')
  })
})
