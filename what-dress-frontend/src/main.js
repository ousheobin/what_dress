import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import echarts from 'echarts'
import './css/index.less'
import './css/element-ui-skin/index.css'

Vue.config.productionTip = false
Vue.prototype.$echarts = echarts

Vue.use(ElementUI)

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
