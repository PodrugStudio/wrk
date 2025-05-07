interface Signal {
  key: string
  params: object | Array<string>
}

interface SignalAction extends Signal {
  function: Function
}

interface LanguageParams {
  default: string
  lang: string
}
interface LanguageResponse extends SignalAction {
  key: string
  // params: object
  // params: Array<String>
  params: LanguageParams
  function: Function
}


const lr: LanguageResponse = {
  key: 'language',
  params: {default: 'en', lang: 'hr'},
  // params: ['de', 'en'],
  function: () => changeLanguage
}

function changeLanguage(params: LanguageParams) {
  console.log('change language', params)
}

console.log(lr);
