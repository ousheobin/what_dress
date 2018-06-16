import Vue from 'vue'
import Router from 'vue-router'
import WelcomePage from '@/page/WelcomePage'
import Result from '@/page/Result'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'WelcomePage',
      component: WelcomePage
    },
    {
      path: '/result',
      name: 'Result',
      component: Result
    }
  ]
})
